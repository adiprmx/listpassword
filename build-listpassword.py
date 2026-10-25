#!/usr/bin/env python3
"""Bangun listpassword.txt dari file sumber resmi SecLists.

Cara pakai:
    python3 build-listpassword.py --sources ./sources-official --output listpassword.txt
    python3 build-listpassword.py --sources ./sources-official --output packs/starter-1000.txt --only 2025-199_most_used_passwords.txt Pwdb_top-1000.txt

Aturan yang dipakai skrip ini (sama seperti file yang sudah jadi di repo):
  1. Urutan file sumber = urutan frekuensi: yang paling umum dibaca duluan.
  2. Buang carriage return (\\r) dan baris kosong.
  3. Dedup sambil menjaga urutan pertama muncul (bukan sort -u, karena
     sort -u menghancurkan urutan paling-umum-dulu).
  4. Jangan pernah menulis komentar ke dalam file password: komentar di
     file password akan ikut dicoba sebagai password.
  5. Skrip ini tidak mengakses internet dan tidak menyimpan password apa pun
     selain yang sudah ada di file sumber.

File sumber yang dipakai paket utama (lihat SOURCES.md untuk URL persisnya):
  - 2025-199_most_used_passwords.txt
  - Pwdb_top-1000.txt
  - 10k-most-common.txt
  - Indonesian_Pwdb_common-password-list-top-150.txt (suplemen, terakhir)
"""
import argparse
import sys
from pathlib import Path

DEFAULT_ORDER = [
    "2025-199_most_used_passwords.txt",
    "Pwdb_top-1000.txt",
    "10k-most-common.txt",
    "Indonesian_Pwdb_common-password-list-top-150.txt",
]


def build(sources_dir: Path, filenames, min_len: int, max_len: int):
    seen = set()
    out = []
    counts = {}
    for name in filenames:
        path = sources_dir / name
        if not path.exists():
            print(f"lewati (tidak ada): {name}", file=sys.stderr)
            continue
        before = len(out)
        with path.open("r", encoding="utf-8", errors="ignore") as f:
            for raw in f:
                line = raw.rstrip("\r\n")
                if not line.strip():
                    continue
                if not (min_len <= len(line) <= max_len):
                    continue
                if line in seen:
                    continue
                seen.add(line)
                out.append(line)
        counts[name] = len(out) - before
    return out, counts


def main() -> int:
    ap = argparse.ArgumentParser(description="Bangun listpassword.txt dari sumber resmi.")
    ap.add_argument("--sources", required=True, help="Folder berisi file sumber SecLists.")
    ap.add_argument("--output", required=True, help="File hasil, mis. listpassword.txt")
    ap.add_argument("--only", nargs="*", default=None,
                    help="Batasi ke file-file ini saja, sesuai urutan yang ditulis.")
    ap.add_argument("--min-len", type=int, default=1)
    ap.add_argument("--max-len", type=int, default=256)
    args = ap.parse_args()

    filenames = args.only if args.only else DEFAULT_ORDER
    lines, counts = build(Path(args.sources), filenames, args.min_len, args.max_len)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"ditulis: {out_path} ({len(lines)} baris)")
    for name, n in counts.items():
        print(f"  +{n} baru dari {name}")
    # Verifikasi mandiri: tidak ada duplikat, tidak ada baris kosong.
    assert len(lines) == len(set(lines)), "duplikat lolos!"
    assert all(line.strip() for line in lines), "baris kosong lolos!"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
