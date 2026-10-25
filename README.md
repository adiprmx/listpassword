# listpassword

Satu file, langsung pakai buat ngecek kekuatan password di lab sendiri.

Bukan katalog raksasa. Repo ini cuma fokus ke satu hal: file `listpassword.txt` yang sudah digabung, sudah dibersihkan, dan sudah diurutkan dari yang paling sering dipakai — jadi lo nggak perlu ngubek-ngubek ribuan file dulu sebelum mulai belajar.

## Baca 30 detik, langsung paham

- **File utama:** `listpassword.txt` — gabungan password paling umum + suplemen Indonesia, satu password per baris, tanpa duplikat, tanpa baris kosong.
- **Paket kecil:** `packs/` — kalau `listpassword.txt` kerasa kegedean, mulai dari yang kecil dulu.
- **Bangun ulang sendiri:** `build-listpassword.py` — gabungin ulang dari sumber daftar umum, kapan pun lo mau. Bukan file sulapan dari entah mana.

## Isi repo

| File | Isi | Baris (terverifikasi) | Buat siapa |
| --- | --- | --- | --- |
| `listpassword.txt` | Paket utama, gabungan + suplemen Indonesia | 10.336 | Yang mau langsung pakai |
| `packs/starter-200.txt` | Tes asap: password paling umum tahunan | 199 | Cek cepat, hitungan detik |
| `packs/starter-1000.txt` | Gabungan 199 tahunan + top-1.000, sudah dedup | 1.094 | Latihan pertama yang serius |
| `packs/starter-10k.txt` | Gabungan 199 + top-1.000 + 10k, sudah dedup | 10.279 | Latihan standar |
| `packs/indonesia-150.txt` | 150 password konteks Indonesia | 150 | Suplemen lokal, bukan pengganti paket global |
| `build-listpassword.py` | Skrip gabung + bersih + dedup, urutan frekuensi dipertahankan | — | Yang mau bangun ulang / ubah filternya |
| `SOURCES.md` | Daftar sumber, nama file persis, tanggal cek | — | Yang mau verifikasi sendiri |
| `docs/CARA-PAKAI.md` | Cara pakai di lab, langkah demi langkah | — | Pemula |
| `docs/BATAS-AMAN.md` | Batas pakai yang nggak boleh dilanggar | — | Semua orang, baca dulu sebelum pakai |
| `docs/APA-BEDA-DENGAN-SECLISTS.md` | Apa yang beda dari katalog besar, apa yang ditambah di sini | — | Yang penasaran kenapa repo ini ada |

Nama paket (`starter-200`, `starter-1000`, `starter-10k`) adalah label tingkat sumbernya, bukan janji jumlah baris persis — jumlah baris asli yang terverifikasi ada di kolom tengah tabel ini. Semua file sudah dicek: 0 duplikat, 0 baris kosong.

## Pakai dalam 3 langkah

1. Baca `docs/BATAS-AMAN.md` dulu. Singkatnya: cuma buat sistem lo sendiri, mesin lab/VM lo sendiri, atau sistem yang sudah ada izin tertulisnya.
2. Ambil file yang sesuai: mulai dari `packs/starter-1000.txt`, naik ke `listpassword.txt` kalau perlu.
3. Uji di lab lo sendiri — misalnya cek apakah password akun tes lo sendiri masuk daftar umum, atau uji hash yang lo buat sendiri di VM.

Contoh bangun ulang:

```bash
python3 build-listpassword.py --sources ./sources-official --output listpassword.txt
```

Skrip ini nggak ngirim apa pun ke internet dan nggak nyimpen password lo. Dia cuma baca file sumber, buang baris kosong, buang duplikat sambil menjaga urutan paling-umum-dulu, lalu nulis hasilnya.

## Yang sengaja nggak ada di sini

- **rockyou.txt (sekitar 14,3 juta password).** Terlalu besar buat repo ini, dan buat pemula itu langkah terakhir, bukan langkah pertama. Kalau suatu hari lo butuh, link resminya ada di `SOURCES.md` — ambil sendiri dari sana, pakai offline lawan hash sendiri.
- **File username:password.** Repo ini cuma daftar password saja, bukan pasangan kredensial.
- **Password beneran siapa pun.** Semua isi di sini adalah password umum yang sudah dipublikasikan buat keperluan tes keamanan. Jangan nambahin password asli lo, password orang lain, atau kata dari dalam sistem target ke file ini.

## Aturan main

- Lab saja. Bukan buat akun, situs, atau layanan orang lain.
- Jangan disemprotkan ke halaman login yang masih hidup. Daftar besar cuma buat kerja offline lawan hash sendiri.
- Kalau nemu password asli yang bocor saat latihan, laporkan lewat jalur yang sudah disepakati sama pemilik sistem, lalu hapus artefak labnya.

Lisensi: MIT. Daftar sumber ada di `SOURCES.md`.
