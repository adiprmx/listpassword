# Sumber

Semua bahan dasar repo ini berasal dari satu proyek resmi: SecLists.

- Proyek: SecLists — "the security tester's companion"
- Pembuat: Daniel Miessler, Jason Haddix, Ignacio Portal, g0tmi1k, dkk
- Repo: https://github.com/danielmiessler/SecLists
- Lisensi: MIT
- Folder password: https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
- Dicek langsung: 25 Oktober 2026 (penelitian deep research) dan diverifikasi ulang saat repo ini dibangun

## File sumber yang dipakai

| File sumber (nama persis) | Peran di repo ini |
| --- | --- |
| `2025-199_most_used_passwords.txt` | Tes asap + awal paket utama |
| `Pwdb_top-1000.txt` | Paket starter-1000 |
| `10k-most-common.txt` | Paket starter-10k + badan paket utama |
| `Language-Specific/Indonesian_Pwdb_common-password-list-top-150.txt` | Suplemen Indonesia (150 baris, diverifikasi langsung) |

File-file di atas tidak ikut divendor mentah-mentah di repo ini. Yang dikirim di sini adalah hasil olahan (gabung + bersih + dedup, urutan frekuensi dipertahankan) lewat `build-listpassword.py`, supaya strukturnya beda dari SecLists dan langsung pakai.

## Yang sengaja tidak diambil

- `rockyou.txt` (~14,3 juta password, dari SecLists `Passwords/Leaked-Databases/`) — terlalu besar untuk repo ini. Sumber resminya: folder Leaked-Databases SecLists di atas, atau paket `wordlists` di Kali Linux (`/usr/share/wordlists/rockyou.txt.gz`). Pakai offline lawan hash sendiri saja.
- File `Default-Credentials` (pasangan `username:password`) — repo ini cuma daftar password saja.
- Daftar dari situs agregator breach (Weakpass, Probable-Wordlists skala besar) — tidak perlu buat paket starter, dan tidak diverifikasi satu per satu di sini.

## Catatan nama file lama

Tutorial lama kadang menyebut `10-million-password-list-top-1000.txt` atau `best110.txt`. Keduanya sudah tidak ada di daftar live SecLists per 25 Oktober 2026. Pengganti resminya sekarang adalah `Pwdb_top-1000.txt` dan `xato-net-10-million-passwords-1000.txt`. Repo ini pakai nama yang sekarang.
