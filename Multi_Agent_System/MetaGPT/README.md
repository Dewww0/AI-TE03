<div align="center">

# MetaGPT — Multi-Agent AI Framework

**Mengubah instruksi dalam bahasa manusia menjadi solusi pengembangan software melalui kolaborasi beberapa agen AI.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9--3.11-blue.svg)](https://www.python.org/)
[![AI](https://img.shields.io/badge/Technology-Multi--Agent%20AI-purple.svg)](https://github.com/geekan/MetaGPT)

</div>

---

## 📌 Tentang Project

**MetaGPT** adalah framework kecerdasan buatan (*Artificial Intelligence*) berbasis **Large Language Models (LLM)** yang menerapkan konsep *Multi-Agent System*. Framework ini memungkinkan beberapa agen AI dengan peran berbeda untuk bekerja sama dalam menyelesaikan tugas yang kompleks, terutama dalam proses analisis kebutuhan, perancangan sistem, pembuatan dokumentasi, dan pengembangan perangkat lunak.

MetaGPT mengadopsi pendekatan simulasi perusahaan pengembang perangkat lunak. Setiap agen AI diberikan tanggung jawab tertentu agar proses kerja dapat dilakukan secara terstruktur dan terkoordinasi.

Sebagai contoh, pengguna cukup memberikan instruksi:

> "Buat aplikasi permainan 2048 menggunakan Python."

Berdasarkan instruksi tersebut, MetaGPT dapat membantu menghasilkan berbagai artefak pengembangan software, seperti kebutuhan sistem, desain arsitektur, struktur data, dokumentasi, dan kode program.

Project ini dikembangkan oleh tim MetaGPT dan tersedia sebagai perangkat lunak open-source.

**Repository resmi:** https://github.com/geekan/MetaGPT

**Dokumentasi resmi:** https://docs.deepwisdom.ai/main/en/

## 🎯 Tujuan Project

MetaGPT dirancang untuk mengeksplorasi bagaimana kolaborasi agen AI dapat digunakan untuk mengotomatisasi dan menyederhanakan proses pengembangan perangkat lunak.

Tujuan utamanya meliputi:

- Mengotomatisasi sebagian tahapan pengembangan perangkat lunak.
- Menerapkan konsep Multi-Agent System dalam pemecahan masalah kompleks.
- Mengintegrasikan Large Language Models ke dalam alur kerja yang terstruktur.
- Menghasilkan artefak pengembangan software berdasarkan instruksi pengguna.
- Meningkatkan koordinasi antara berbagai peran AI dalam menyelesaikan suatu tugas.
- Menyediakan framework yang dapat dikembangkan untuk berbagai kebutuhan aplikasi berbasis AI.

## ✨ Fitur Utama

### 1. Multi-Agent Collaboration

MetaGPT memungkinkan beberapa agen AI bekerja sama dengan peran dan tanggung jawab yang berbeda.

Pendekatan ini membantu membagi pekerjaan kompleks menjadi beberapa tahapan yang lebih terstruktur.

### 2. Software Development Automation

MetaGPT dapat membantu proses pengembangan perangkat lunak, mulai dari memahami kebutuhan pengguna hingga menghasilkan kode dan dokumentasi proyek.

### 3. Role-Based AI Agents

Framework ini menyediakan pendekatan berbasis peran yang menyerupai struktur tim pengembangan software profesional.

Beberapa peran yang disimulasikan antara lain:

| Peran | Tanggung Jawab |
|---|---|
| Product Manager | Membantu mengidentifikasi kebutuhan dan tujuan produk. |
| Architect | Membantu merancang arsitektur dan struktur sistem. |
| Project Manager | Membantu mengatur tahapan dan pembagian pekerjaan. |
| Engineer | Membantu mengimplementasikan solusi dalam bentuk kode program. |

Ketersediaan dan perilaku setiap peran bergantung pada implementasi serta alur kerja yang digunakan.

### 4. Large Language Model Integration

MetaGPT mendukung integrasi dengan berbagai penyedia model bahasa melalui konfigurasi yang sesuai.

Pilihan penyedia model dan kompatibilitasnya bergantung pada versi framework serta konfigurasi yang digunakan.

### 5. Data Interpreter

MetaGPT juga menyediakan komponen Data Interpreter yang dapat membantu menjalankan tugas terkait pemrograman, analisis data, dan visualisasi.

Contohnya adalah melakukan analisis dataset menggunakan Python dan menghasilkan grafik berdasarkan instruksi pengguna.

### 6. Extensible Framework

Struktur MetaGPT memungkinkan pengembang mempelajari implementasi agen, menyesuaikan alur kerja, dan mengembangkan kemampuan tambahan sesuai kebutuhan.

---

## 🧠 Konsep dan Arsitektur Sistem

MetaGPT menggunakan pendekatan Multi-Agent System yang menggabungkan model bahasa dengan pembagian peran, pesan antarkomponen, serta alur kerja yang terstruktur.

Secara konseptual, alur kerjanya dapat digambarkan sebagai berikut:

```text
             USER INPUT
                  |
                  v
        +-------------------+
        | Natural Language  |
        | Requirements      |
        +-------------------+
                  |
                  v
        +-------------------+
        | Multi-Agent       |
        | Workflow          |
        +-------------------+
                  |
         +--------+--------+
         |        |        |
         v        v        v
      Product  Architect  Project
      Manager             Manager
         |        |        |
         +--------+--------+
                  |
                  v
        +-------------------+
        | Engineering and   |
        | Implementation    |
        +-------------------+
                  |
                  v
        +-------------------+
        | Generated Code,   |
        | Documents, and    |
        | Project Artifacts |
        +-------------------+
```

*Diagram tersebut merupakan gambaran konseptual, bukan representasi lengkap dari seluruh jalur eksekusi internal MetaGPT.*

### Komponen Utama

**1. User Input**

Pengguna memberikan instruksi atau kebutuhan dalam bahasa alami.

**2. Multi-Agent Workflow**

Framework mengatur proses pengerjaan dan koordinasi agen sesuai alur kerja yang digunakan.

**3. Role-Based Agents**

Setiap agen menjalankan tugas berdasarkan peran dan instruksi yang diberikan.

**4. Large Language Model**

LLM digunakan untuk membantu memahami instruksi, melakukan penalaran, menghasilkan konten, dan menyusun keluaran yang diperlukan.

**5. Project Artifacts**

Hasil pengerjaan dapat mencakup kode program, dokumentasi, desain sistem, dan berkas proyek lainnya.

Perlu diperhatikan bahwa hasil yang dihasilkan AI tidak selalu benar atau langsung dapat digunakan. Pengujian dan pemeriksaan oleh manusia tetap diperlukan.

---

## 🛠️ Teknologi yang Digunakan

MetaGPT dibangun menggunakan ekosistem Python dan berbagai pustaka pendukung.

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama. |
| Large Language Models | Pemrosesan bahasa alami dan generasi konten. |
| OpenAI API | Integrasi dengan model yang kompatibel. |
| Anthropic API | Integrasi dengan model yang didukung. |
| Pydantic | Validasi dan pengelolaan struktur data. |
| NumPy | Operasi numerik. |
| Pandas | Pengolahan dan analisis data. |
| Scikit-learn | Fungsionalitas machine learning tertentu. |
| Git | Pengelolaan versi kode sumber. |

Daftar tersebut merupakan contoh teknologi yang terdapat dalam ekosistem dependensi proyek, bukan berarti seluruh teknologi wajib digunakan dalam setiap eksekusi.

---

## 📋 Persyaratan Sistem

Sebelum melakukan instalasi, pastikan lingkungan pengembangan memenuhi persyaratan berikut.

- **Python:** versi 3.9 atau lebih baru, tetapi di bawah 3.12 untuk panduan instalasi pada README ini.
- **Git:** untuk mengunduh repository.
- **Node.js:** diperlukan untuk penggunaan tertentu.
- **pnpm:** diperlukan untuk penggunaan tertentu.
- **API Key:** diperlukan apabila menggunakan penyedia LLM eksternal yang membutuhkan autentikasi.
- **Koneksi internet:** diperlukan untuk instalasi dependensi dan akses layanan eksternal sesuai konfigurasi.

Kompatibilitas aktual dapat berbeda berdasarkan versi MetaGPT, sistem operasi, dan penyedia model yang digunakan.

---

## 🚀 Instalasi

### 1. Clone Repository

Buka terminal atau Command Prompt, kemudian jalankan:

```bash
git clone https://github.com/geekan/MetaGPT.git
```

Masuk ke direktori proyek:

```bash
cd MetaGPT
```

### 2. Buat Virtual Environment

Disarankan menggunakan virtual environment agar dependensi proyek tidak bercampur dengan instalasi Python lainnya.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux atau macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Pastikan versi Python sesuai dengan persyaratan proyek.

### 3. Instal MetaGPT

Untuk instalasi dari source code:

```bash
pip install --upgrade pip
pip install -e .
```

Jika instalasi editable mengalami masalah dependensi, periksa dokumentasi instalasi resmi untuk langkah yang sesuai dengan versi repository.

### 4. Inisialisasi Konfigurasi

Jalankan perintah berikut:

```bash
metagpt --init-config
```

Perintah tersebut akan membuat berkas konfigurasi pengguna di lokasi default MetaGPT.

Lokasi konfigurasi default:

```text
~/.metagpt/config2.yaml
```

Lokasi ini umumnya berada di direktori home pengguna. Pada Windows, direktori home berbeda sesuai akun dan lingkungan yang digunakan.

---

## ⚙️ Konfigurasi API

MetaGPT memerlukan konfigurasi model bahasa agar dapat menjalankan tugas yang menggunakan LLM.

Buka berkas konfigurasi:

```text
~/.metagpt/config2.yaml
```

Contoh konfigurasi dasar untuk penyedia yang kompatibel dengan OpenAI API:

```yaml
llm:
  api_type: "openai"
  model: "gpt-4-turbo"
  base_url: "https://api.openai.com/v1"
  api_key: "YOUR_API_KEY"
```

Sesuaikan nilai konfigurasi dengan model dan penyedia layanan yang benar-benar digunakan.

**Penting:**

- Ganti `YOUR_API_KEY` dengan API key milik sendiri.
- Jangan mengunggah API key ke repository publik.
- Jangan menaruh API key langsung di kode yang akan dibagikan.
- Pastikan model yang dipilih masih tersedia dan dapat diakses melalui akun penyedia.
- Untuk penyedia selain OpenAI, ikuti contoh konfigurasi dan dokumentasi resmi MetaGPT.

API key merupakan kredensial rahasia. Jika tidak sengaja terpublikasi, segera cabut atau rotasi kredensial tersebut melalui penyedia layanan terkait.

---

## 💻 Cara Menggunakan

### 1. Menggunakan Command Line Interface (CLI)

Setelah instalasi dan konfigurasi selesai, MetaGPT dapat dijalankan melalui terminal.

Contoh:

```bash
metagpt "Create a 2048 game"
```

Instruksi tersebut meminta MetaGPT membantu membuat permainan 2048.

Hasil yang dihasilkan akan ditempatkan pada direktori workspace sesuai perilaku dan konfigurasi framework.

Pengguna dapat mengganti instruksi dengan kebutuhan lain, misalnya:

```bash
metagpt "Create a simple task management application"
```

Contoh lain:

```bash
metagpt "Create a Python program for analyzing CSV data"
```

Hasil akhir bergantung pada konfigurasi LLM, instruksi yang diberikan, dan kemampuan agen yang digunakan.

### 2. Menggunakan MetaGPT melalui Python

MetaGPT juga dapat digunakan sebagai library dalam program Python.

Contoh penggunaan API tingkat tinggi yang tersedia pada framework:

```python
from metagpt.software_company import generate_repo
from metagpt.utils.project_repo import ProjectRepo

repo: ProjectRepo = generate_repo(
    "Create a 2048 game"
)

print(repo)
```

Kode tersebut meminta MetaGPT menghasilkan repository berdasarkan instruksi yang diberikan, kemudian menampilkan representasi objek repository.

Pastikan paket sudah terinstal dan konfigurasi LLM sudah tersedia sebelum menjalankan program.

### 3. Menggunakan Data Interpreter

Data Interpreter merupakan komponen yang dapat digunakan untuk membantu menjalankan tugas pemrograman dan analisis data.

Contoh:

```python
import asyncio

from metagpt.roles.di.data_interpreter import DataInterpreter


async def main():
    interpreter = DataInterpreter()

    await interpreter.run(
        "Run data analysis on sklearn Iris dataset, include a plot"
    )


if __name__ == "__main__":
    asyncio.run(main())
```

Contoh tersebut meminta Data Interpreter melakukan analisis dataset Iris menggunakan scikit-learn dan menyertakan visualisasi.

Keberhasilan eksekusi bergantung pada dependensi yang tersedia, konfigurasi model, serta lingkungan eksekusi.

---

## 📁 Struktur Direktori

Berikut gambaran struktur utama repository MetaGPT:

```text
MetaGPT/
│
├── config/
│   ├── config2.example.yaml
│   └── examples/
│
├── docs/
│   ├── README_CN.md
│   ├── README_FR.md
│   ├── README_JA.md
│   ├── FAQ-EN.md
│   └── ACADEMIC_WORK.md
│
├── examples/
│   └── ...
│
├── metagpt/
│   └── ...
│
├── tests/
│   └── ...
│
├── Dockerfile
├── LICENSE
├── MANIFEST.in
├── README.md
└── requirements.txt
```

Struktur di atas merupakan ringkasan direktori utama. Isi dan susunan direktori dapat berbeda menurut versi repository.

### Penjelasan Direktori

| Direktori atau Berkas | Fungsi |
|---|---|
| `config/` | Contoh konfigurasi dan konfigurasi untuk berbagai penyedia model. |
| `docs/` | Dokumentasi, panduan, FAQ, dan referensi akademik. |
| `examples/` | Contoh implementasi dan penggunaan framework. |
| `metagpt/` | Implementasi utama framework MetaGPT. |
| `tests/` | Pengujian kode untuk komponen proyek. |
| `Dockerfile` | Instruksi untuk membangun image Docker. |
| `LICENSE` | Ketentuan lisensi perangkat lunak. |
| `README.md` | Dokumentasi pengenalan dan panduan penggunaan. |
| `requirements.txt` | Daftar dependensi Python yang digunakan proyek. |

---

## 🔬 Contoh Kasus Penggunaan

MetaGPT dapat digunakan untuk mempelajari dan mengeksplorasi berbagai penerapan sistem AI berbasis agen.

### 1. Otomatisasi Pengembangan Software

Pengguna memberikan deskripsi aplikasi yang ingin dibuat. Agen AI kemudian membantu menyusun kebutuhan, rancangan, dan implementasi perangkat lunak.

### 2. Pembuatan Dokumentasi Teknis

MetaGPT dapat membantu menghasilkan dokumen kebutuhan perangkat lunak, rancangan sistem, struktur data, dan dokumentasi pendukung.

### 3. Analisis Data

Melalui Data Interpreter, pengguna dapat memberikan instruksi analisis data yang melibatkan pemrosesan dataset, pembuatan kode, dan visualisasi.

### 4. Eksperimen Multi-Agent AI

Repository ini dapat digunakan sebagai bahan pembelajaran untuk memahami pembagian peran agen, koordinasi tugas, penggunaan LLM, serta pengembangan alur kerja AI.

### 5. Riset dan Pengembangan

Pengembang dapat mempelajari arsitektur framework dan menggunakannya sebagai dasar eksperimen pada bidang agentic AI, otomatisasi, dan rekayasa perangkat lunak.

---

## ⚠️ Batasan dan Hal yang Perlu Diperhatikan

Meskipun MetaGPT dapat membantu mengotomatisasi sebagian pekerjaan, terdapat sejumlah hal yang perlu diperhatikan.

- **Ketergantungan pada LLM:** kualitas hasil bergantung pada model, prompt, dan konfigurasi yang digunakan.
- **Biaya penggunaan API:** penyedia model tertentu mengenakan biaya berdasarkan penggunaan.
- **Potensi kesalahan:** kode dan dokumen yang dihasilkan AI dapat mengandung kesalahan.
- **Kebutuhan sumber daya:** instalasi serta penggunaan dependensi dapat membutuhkan ruang penyimpanan dan sumber daya komputasi yang cukup.
- **Keamanan kode:** kode hasil generasi AI perlu diperiksa sebelum dijalankan, terutama jika berinteraksi dengan sistem operasi, jaringan, atau data penting.
- **Kompatibilitas versi:** perubahan API dan dependensi dapat memengaruhi proses instalasi maupun eksekusi.

Oleh karena itu, hasil MetaGPT sebaiknya diperlakukan sebagai keluaran yang perlu ditinjau, diuji, dan divalidasi.

---

## 📚 Referensi dan Dokumentasi

Untuk mempelajari MetaGPT lebih lanjut, kunjungi sumber berikut:

- **Repository resmi:** https://github.com/geekan/MetaGPT
- **Dokumentasi resmi:** https://docs.deepwisdom.ai/main/en/
- **Panduan instalasi:** https://docs.deepwisdom.ai/main/en/guide/get_started/installation.html
- **Panduan penggunaan:** https://docs.deepwisdom.ai/main/en/guide/get_started/quickstart.html
- **Tutorial Agent 101:** https://docs.deepwisdom.ai/main/en/guide/tutorials/agent_101.html
- **Tutorial Multi-Agent 101:** https://docs.deepwisdom.ai/main/en/guide/tutorials/multi_agent_101.html
- **Referensi akademik:** https://openreview.net/forum?id=VtmBAGCN7o

Referensi tersebut dapat digunakan untuk memahami konsep, implementasi, dan perkembangan framework lebih lanjut.

---

## 🤝 Kontribusi

Kontribusi terhadap pengembangan proyek open-source dapat dilakukan dengan mempelajari kode, memperbaiki bug, menyempurnakan dokumentasi, atau mengembangkan fitur baru.

Untuk berkontribusi:

1. Pelajari struktur dan pedoman kontribusi repository.
2. Buat branch untuk perubahan yang akan dilakukan.
3. Implementasikan perubahan dengan tetap mengikuti standar proyek.
4. Jalankan pengujian yang relevan.
5. Ajukan Pull Request sesuai prosedur repository.

Untuk panduan kontribusi yang lebih lengkap, silakan merujuk pada dokumentasi resmi dan pedoman kontribusi di repository MetaGPT.

---

## 📄 Lisensi

MetaGPT menggunakan lisensi **MIT**, sesuai dengan berkas `LICENSE` yang tersedia dalam repository.

Lisensi MIT memberikan izin penggunaan, penyalinan, modifikasi, distribusi, dan sublicensing perangkat lunak dengan tetap memenuhi ketentuan lisensi, termasuk penyertaan pemberitahuan hak cipta dan lisensi yang berlaku.

Sebelum mendistribusikan versi yang telah dimodifikasi, pastikan ketentuan lisensi dipenuhi dan asal-usul proyek dijelaskan dengan benar.

---

## ⭐ Penutup

MetaGPT merupakan contoh penerapan Multi-Agent System yang menggabungkan Large Language Models dengan alur kerja berbasis peran untuk membantu menyelesaikan tugas pengembangan perangkat lunak.

Melalui framework ini, pengembang dapat mempelajari bagaimana agen AI berkolaborasi, bagaimana instruksi bahasa alami diterjemahkan menjadi artefak software, dan bagaimana proses pengembangan berbasis AI dapat dieksplorasi lebih lanjut.

Jika project ini bermanfaat, kunjungi repository resmi untuk mempelajari implementasi, dokumentasi, dan perkembangan terbarunya.

**Repository:** https://github.com/geekan/MetaGPT

---
