# Implementasi Metode Vektor Ruang pada Sistem Search Engine untuk Pencarian Jurnal

Proyek ini merupakan implementasi dari metode vektor ruang untuk sistem pencarian jurnal menggunakan teknik aljabar linear, khususnya terkait dengan konsep-konsep seperti **TF-IDF** (Term Frequency-Inverse Document Frequency) dan **cosine similarity**. Proyek ini dikembangkan oleh tiga orang anggota yang memiliki fokus pada penerapan vektor ruang dalam konteks pencarian berbasis teks.

## Anggota Kelompok
1. Anggota 1: Fajar Geran Arifin (237006079)
2. Anggota 2: Farid Firdaus (237006081)
3. Anggota 3: Fadhil Gani (237006082)

## Deskripsi Proyek
Tujuan dari proyek ini adalah untuk mengembangkan sebuah sistem pencarian jurnal yang menggunakan metode **Vektor Ruang**. Dengan menggunakan konsep aljabar linear, kami akan mengimplementasikan metode **TF-IDF** untuk representasi dokumen, serta menggunakan **cosine similarity** untuk mengukur relevansi antara query pencarian dan dokumen-dokumen yang ada dalam database.

### Fitur Utama:
- **Pencarian Berdasarkan Query**: Pengguna dapat mencari jurnal dengan memasukkan kata kunci.
- **Pengurutan Berdasarkan Kriteria**: Hasil pencarian dapat diurutkan berdasarkan relevansi, tahun, atau jumlah sitasi.
- **Filter Berdasarkan Tahun**: Pengguna dapat memfilter jurnal berdasarkan rentang tahun tertentu (misalnya 3 tahun terakhir, 5 tahun terakhir, dll).

## Struktur Proyek
Proyek ini dibangun menggunakan framework **Flask** untuk backend dan HTML/JavaScript untuk frontend. Berikut adalah struktur direktori proyek:

```
/tugas-akhir
|-- /app
|   |-- init.py
|   |-- routes.py
|   |-- search_paper.py
|-- /static
|   |-- output.css
|-- /templates
|   |-- index.html
|-- app.py
|-- main.py
|-- README.md
|-- tailwind.config.js
```

### Penjelasan Struktur:
- **/app**: Berisi file Python yang mengatur logika aplikasi (infrastruktur, rute, dan pencarian).
- **/static**: Menyimpan file statis seperti CSS atau JavaScript yang digunakan pada frontend.
- **/templates**: Menyimpan file HTML untuk tampilan frontend.
- **app.py**: File utama untuk menjalankan aplikasi Flask.
- **main.py**: Menjalankan aplikasi Flask dari `create_app()`.
- **tailwind.config.js**: File konfigurasi untuk **Tailwind CSS**.

## Instalasi
Ikuti langkah-langkah berikut untuk menjalankan proyek ini secara lokal:

### 1. Clone repositori ini:
```bash
git clone <URL_REPOSITORY>
cd tugas-akhir
```

### 2. Buat dan aktifkan virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Di Linux/macOS
venv\Scripts\activate     # Di Windows
```

### 3. Instal dependensi:
```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi:
```bash
python app.py
```
Aplikasi akan berjalan di `http://127.0.0.1:5000`.

## Cara Kerja
### 1. Pengumpulan Data Jurnal
Data jurnal yang digunakan dalam sistem ini berasal dari **Kaggle**. Dataset yang digunakan adalah **Research Papers Dataset (Version 10)** yang mencakup berbagai jurnal ilmiah di berbagai bidang studi seperti komputer sains, matematika, fisika, dan lainnya.

Dataset ini mengandung berbagai atribut dan metadata dari setiap jurnal, seperti:
- **id**: ID unik untuk setiap jurnal.
- **title**: Judul jurnal.
- **authors**: Daftar penulis jurnal.
- **venue**: Nama jurnal atau tempat publikasi.
- **year**: Tahun publikasi.
- **n_citation**: Jumlah sitasi yang diterima jurnal.
- **references**: Daftar ID jurnal yang dikutip oleh jurnal ini.
- **abstract**: Abstrak jurnal.

Dataset ini bisa diunduh melalui [Kaggle - Research Papers Dataset](https://www.kaggle.com/datasets/nechbamohammed/research-papers-dataset/data).

Setelah diunduh, data jurnal ini dimasukkan ke dalam database **MongoDB** yang digunakan untuk penyimpanan dan pengambilan data dalam aplikasi pencarian jurnal.

### 2. Representasi Dokumen
Setiap dokumen diproses dengan menghitung **TF-IDF** untuk setiap kata dalam abstrak dan judul jurnal. Hasil dari proses ini adalah representasi vektor dari setiap dokumen.

### 3. Pencocokan Query
Ketika pengguna memasukkan kata kunci (query), query ini juga diproses menjadi vektor menggunakan metode **TF-IDF** yang sama. Kemudian, dilakukan perhitungan **cosine similarity** antara query dan dokumen-dokumen yang ada dalam database untuk menentukan relevansi setiap dokumen dengan query yang diberikan.

### 4. Pengurutan dan Penyaringan
Hasil pencarian kemudian diurutkan berdasarkan kriteria yang dipilih oleh pengguna: relevansi, tahun, atau jumlah sitasi. Pengguna juga dapat memfilter hasil berdasarkan rentang tahun yang dipilih.

## Teknologi yang Digunakan
- **Flask**: Framework web Python untuk membangun aplikasi backend.
- **MongoDB**: Database NoSQL untuk menyimpan data jurnal.
- **scikit-learn**: Library Python untuk menghitung **TF-IDF** dan **cosine similarity**.
- **HTML/CSS/JavaScript**: Untuk pengembangan antarmuka pengguna.
- **Tailwind CSS**: Framework CSS untuk mempercepat pengembangan antarmuka pengguna dengan menggunakan utility-first CSS.

## Pengujian
Untuk menguji sistem ini, Anda bisa mencoba beberapa pencarian jurnal berdasarkan kata kunci. Berikut adalah beberapa contoh:

- Query: **"linear algebra"**
- Sort By: **Relevance**
- Year Filter: **5 Years**

Cek hasil pencarian untuk melihat apakah jurnal yang relevan muncul dengan benar dan hasilnya terurut sesuai dengan preferensi pengguna.

## Kontribusi
Kontribusi sangat diterima! Jika Anda ingin membantu mengembangkan proyek ini, silakan buka issue atau buat pull request. Kami akan dengan senang hati menerima masukan dan perbaikan.
