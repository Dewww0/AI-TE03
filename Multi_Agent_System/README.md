
# Multi-Agent System (MAS)

## Deskripsi
Multi-Agent System (MAS) adalah sistem yang terdiri dari beberapa agen
yang berinteraksi dan bekerja sama untuk mencapai tujuan tertentu.

Program ini merupakan simulasi kerja sama agen untuk menyelesaikan
sebuah proyek menggunakan bahasa pemrograman Python.

## Tujuan
- Memahami konsep dasar Multi-Agent System.
- Mempelajari cara beberapa agen berkomunikasi dan bekerja sama.
- Menunjukkan pembagian tugas di antara agen yang berbeda.
- Melakukan evaluasi terhadap hasil pekerjaan.

## Agen dalam Sistem

### 1. Planner Agent
Bertugas merencanakan proyek dan membagi pekerjaan menjadi beberapa tugas.
Tugas utama Planner Agent:
1. Menerima informasi mengenai proyek yang akan dikerjakan.
2. Menyusun rencana pengerjaan proyek.
3. Membagi proyek menjadi beberapa tugas.
4. Menentukan daftar pekerjaan yang perlu dilaksanakan oleh Worker Agent.

### 2. Worker Agent
Bertugas mengerjakan tugas yang diberikan oleh Planner Agent.
Tugas utama Worker Agent:
1. Menerima daftar tugas dari Planner Agent.
2. Memproses tugas yang telah diberikan.
3. Menghasilkan status atau hasil pengerjaan setiap tugas.
4. Menyediakan informasi hasil pekerjaan untuk diperiksa oleh Evaluator Agent.

### 3. Evaluator Agent
Bertugas memeriksa status seluruh tugas dan menentukan hasil akhir proyek.
Tugas utama Evaluator Agent:
1. Memeriksa status setiap tugas yang telah diproses.
2. Mengevaluasi kelengkapan pengerjaan tugas.
3. Menentukan status akhir proyek berdasarkan hasil pemeriksaan.
4. Memberikan informasi mengenai hasil evaluasi proyek.

## Alur Kerja
1. Sistem menerima nama proyek.
2. Planner Agent membagi proyek menjadi beberapa tugas.
3. Worker Agent mengerjakan setiap tugas.
4. Setiap agen memproses tugas yang diberikan secara mandiri.
5. Evaluator Agent memeriksa hasil pekerjaan.
6. Sistem menampilkan status akhir proyek.

## Teknologi
1. Bahasa Pemrograman: Python 3
Python digunakan untuk mengimplementasikan logika sistem, mengatur alur kerja, dan menjalankan fungsi setiap agen.

2. Library: Python Standard Library
Pustaka bawaan Python digunakan untuk mendukung fungsi dasar program tanpa harus bergantung pada pustaka eksternal tambahan, selama implementasinya memang hanya menggunakan pustaka standar.

3. Platform: GitHub
GitHub digunakan sebagai tempat penyimpanan kode sumber, dokumentasi, dan pengelolaan versi proyek.

## Cara Menjalankan

Pastikan Python 3 sudah terinstal.

Jalankan perintah berikut melalui terminal:

```bash
python main.py
```

Pada beberapa sistem, gunakan:

```bash
python3 main.py
```

## Contoh Proyek
Pembuatan Sistem Informasi Sederhana.

## Hasil yang Diharapkan
Program menampilkan proses perencanaan, pengerjaan, dan evaluasi
tugas hingga menghasilkan status akhir proyek.

## Pengembang
| No. | Name | Student ID (NIM) | GitHub Username | Role |
|---:|---|---|---|---|
| 1 | Deo Ferdiyansyah | 101022430007 | @dewww0 | Manager |
| 2 | Tegar Pambudi Hutomo | 101022400219 | @tegarph | Dev_1 |
| 3 | M Amhari Septianto | 101022400119 | @muhamharisept-alt | Dev_2 |

## Kesimpulan
Program ini menunjukkan konsep dasar Multi-Agent System melalui
pembagian tanggung jawab antara agen perencana, agen pekerja,
dan agen evaluator untuk mencapai tujuan bersama.

