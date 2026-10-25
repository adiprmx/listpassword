# Apa beda repo ini dengan SecLists?

SecLists itu katalog lengkap buat security tester: ribuan file di banyak kategori
(Discovery, Fuzzing, Usernames, Passwords, dan seterusnya). Repo ini sengaja
tidak meniru itu.

## Yang beda

| SecLists | Repo ini |
| --- | --- |
| Katalog besar, banyak kategori | Satu fokus: `listpassword.txt` yang langsung pakai |
| Struktur `Passwords/Common-Credentials/...` | Struktur datar: file utama di root, paket di `packs/`, dok di `docs/` |
| Lo yang gabungin sendiri filenya | File gabungan sudah jadi + skrip bangun ulangnya |
| Bahasa Inggris, dokumentasi proyek besar | Dokumentasi Indonesia, pendek, langkah demi langkah |
| Tidak ada file bernama `listpassword.txt` | `listpassword.txt` adalah produk utamanya |
| Tidak ada suplemen Indonesia yang digabung | Suplemen Indonesia 150 baris sudah digabung ke paket utama, plus tersedia terpisah |

## Yang ditambah di sini

1. `listpassword.txt` itu sendiri — SecLists tidak mengirim file dengan nama ini.
2. Paket bertingkat: starter-200, starter-1000, starter-10k — jadi pemula tidak langsung tenggelam di daftar raksasa.
3. Suplemen Indonesia yang terintegrasi, bukan sekadar file terpisah di folder Language-Specific.
4. Skrip bangun ulang yang menjaga urutan paling-umum-dulu (dedup tanpa `sort -u`).
5. Dokumen batas aman dan cara pakai lab yang eksplisit, berbahasa Indonesia.

## Yang tetap sama dan diakui

Bahan dasarnya tetap SecLists, lisensi MIT, atribusi lengkap di `ATTRIBUTION.md`
dan `SOURCES.md`. Repo ini tidak mengklaim SecLists sebagai karyanya.
