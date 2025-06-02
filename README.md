# EduQuiz

**EduQuiz** adalah aplikasi web simulasi quiz edukatif interaktif berbasis Python Flask, HTML, dan CSS.  
Aplikasi ini dirancang untuk mengimplementasikan beberapa teknik konstruksi perangkat lunak modern seperti:  
- State-based/Automata
- Table-driven
- Code reuse
- Runtime configuration
- Design Pattern (Singleton, Facade)

## Struktur Folder
<pre>
EduQuiz/
│
├── app.py
│
├── README.md
│
├── soal_config.json
│
├── src/
│   ├── __init__.py
│   ├── question_loader.py
│   ├── state_machine.py
│   ├── quiz_manager.py
│   └── config.py
│
├── static/
│   ├── config/
│   │   └── soal_config.json
│   ├── css/
│   │   ├── home.css
│   │   ├── quiz.css
│   │   ├── result.css
│   │   └── about.css
│   ├── img/
│   │   └── sample.png
│   └── logo/
│       └── logo.png
│
├── templates/
│   ├── home.html
│   ├── quiz.html
│   ├── result.html
│   └── about.html
</pre>

## Penugasan Tim (4 Anggota)
| Anggota     | Tanggung Jawab                 | File HTML         | File CSS       |
| ----------- | ------------------------------ | ----------------- | -------------- |
| Hamid       | Beranda / Home                 | home.html         | home.css       |
| Ancha       | Halaman Quiz                   | quiz.html         | quiz.css       |
| Ricky       | Hasil / Result                 | result.html       | result.css     |
| Dava        | Tentang / About                | about.html        | about.css      |

## Cara Menjalankan
1. Pastikan sudah install `flask` (`pip install flask`)
2. Jalankan dengan:
    ```
    python app.py
    ```
3. Akses di browser: [http://localhost:5000](http://localhost:5000)

## Palet Warna
- Background: `#FFFFFF`
- Primary: `#FFA500`
- Accent: `#007FFF`
- Text: `#000000`
- bg-200: `#f5f5f5`
- primary-200: `dd8900`
- primary-300: `904a00`
- accent-200: `e0ffff`
- text-200: `#2c2c2c`

## Design Pattern yang Diimplementasi
- **Singleton** (di file `src/config.py`)
- **Facade** (di file `src/quiz_manager.py`)

## Standar Clean Code & Secure Coding
- Pemisahan kode logic, resource, dan view
- Validasi input user (required, strip, lower-case compare)
- Session handling yang aman
- Tidak menyimpan jawaban benar di client/browser

---

Tim EduQuiz - 2025