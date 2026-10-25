# Cara pakai

Baca `BATAS-AMAN.md` dulu sebelum menjalankan apa pun.

## 1. Pilih file yang sesuai

- Baru mulai: `packs/starter-1000.txt`
- Sudah nyaman: `listpassword.txt`
- Mau cek pola lokal saja: `packs/indonesia-150.txt` sebagai tambahan, bukan pengganti paket global

## 2. Pakai di lab sendiri saja

Contoh yang sah:

- Buat akun tes di VM lo sendiri, lalu cek apakah password akun tes itu masuk daftar umum.
- Buat hash dari password tes lo sendiri di VM, lalu uji hash itu secara offline dengan daftar ini.

Contoh yang tidak sah: mencoba daftar ini ke akun, situs, atau layanan milik orang lain, atau ke halaman login yang masih hidup.

## 3. Bangun ulang kalau mau mengubah

```bash
python3 build-listpassword.py --sources ./sources-official --output listpassword.txt
```

Ganti `--output` dan `--only` kalau lo cuma mau paket kecil:

```bash
python3 build-listpassword.py --sources ./sources-official \
  --output packs/starter-1000.txt \
  --only 2025-199_most_used_passwords.txt Pwdb_top-1000.txt
```

## 4. Verifikasi file hasil

```bash
wc -l listpassword.txt
sort listpassword.txt | uniq -d | wc -l   # harus 0, artinya tidak ada duplikat
grep -c '^$' listpassword.txt            # harus 0, artinya tidak ada baris kosong
```

## Jangan lakukan ini

- Jangan ketik password asli akun produksi lo ke skrip atau alat apa pun buat "ngecek".
- Jangan menambahkan password asli, nama orang, atau kata internal dari sistem target ke daftar ini.
- Jangan mengunggah file hasil latihan yang berisi temuan akun asli ke repo publik.
