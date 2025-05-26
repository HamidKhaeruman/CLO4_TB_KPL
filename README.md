# EduQuiz UI - Proyek Antarmuka Web Edukasi Interaktif

EduQuiz adalah aplikasi kuis edukatif berbasis web yang dirancang dengan HTML dan CSS. Proyek ini merupakan bagian dari pengembangan EduQuiz versi CLI menjadi web yang lebih interaktif, terstruktur, dan mudah digunakan.

## 📁 Struktur Folder

Berikut adalah struktur folder yang digunakan dalam proyek ini:

<pre>
EduQuiz_UI/
├── templates/
│   ├── index.html          # Halaman utama / beranda
│   ├── quiz.html           # Halaman kuis (soal & pilihan jawaban)
│   ├── result.html         # Halaman hasil kuis
│   ├── category.html       # Halaman daftar kategori kuis
│   └── about.html          # Halaman tentang aplikasi dan tim
│
├── assets/
│   ├── css/
│   │   └── style.css       # File CSS utama untuk styling
│   └── images/             # Folder untuk gambar (logo, ikon, ilustrasi, dsb)
│
└── README.md               # Dokumentasi proyek
</pre>

## 🎨 Palet Warna

Proyek ini menggunakan palet warna lembut dan profesional untuk meningkatkan kenyamanan visual pengguna:

| Nama Warna   | HEX        |
|--------------|------------|
| Dark Maroon  | `#432729`  |
| Charcoal     | `#534F54`  |
| Bronze       | `#A37949`  |
| Sand         | `#F2D598`  |
| Cream        | `#F5EED7`  |

## 📑 Deskripsi Tiap Halaman

- **`index.html`**: Menampilkan pengantar dan tombol mulai kuis.
- **`quiz.html`**: Halaman kuis interaktif dengan soal dan opsi jawaban.
- **`result.html`**: Menampilkan skor dan evaluasi hasil kuis.
- **`category.html`**: Pengguna memilih kategori kuis sebelum mulai.
- **`about.html`**: Informasi tentang aplikasi dan pengembangnya.

## 📌 Catatan Tambahan

- File HTML berada dalam folder `templates/` agar siap digunakan bersama framework seperti Flask atau Django.
- Aset statis seperti CSS dan gambar ditempatkan dalam folder `assets/` untuk kemudahan manajemen.

## 🚀 Cara Menggunakan

Cukup buka `templates/index.html` di browser untuk mulai menjelajahi tampilan.

Untuk integrasi dinamis (misal dengan Python/Flask), pastikan file CSS dapat diakses dari `static/` jika kamu ubah struktur lebih lanjut.

---

> Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Rekayasa Perangkat Lunak. Tujuan utamanya adalah meningkatkan pengalaman belajar melalui media digital yang interaktif dan menyenangkan.
