# 🇮🇩 Indonesian Population Prediction

Prediksi jumlah populasi penduduk Indonesia menggunakan model **Linear Regression** sederhana berbasis **scikit-learn**. Repositori ini menyajikan eksperimen pemodelan data tren demografi beserta antarmuka simulasi interaktif menggunakan **Streamlit**.

---

## 📌 Catatan Data

Data populasi yang digunakan dikumpulkan pada tahun **2021** dan tersimpan di dalam direktori `data/`.

> **Catatan:** Sumber data asli saat ini tidak terdokumentasi secara spesifik karena tautan sumber asli sudah tidak aktif/tersedia saat dicari kembali.

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Prasyarat & Instalasi
Pastikan Python sudah terinstal di komputer Anda. Pasang pustaka yang diperlukan dengan menjalankan perintah berikut di terminal:

```bash
pip install streamlit scikit-learn pandas numpy
```

### 2. Jalankan Simulasi Streamlit
Eksekusi perintah berikut untuk membuka antarmuka simulasi di peramban web Anda:

```bash
streamlit run main.py
```

---

## 📂 Struktur Repositori

```text
.
├── data/           # Dataset populasi penduduk Indonesia
├── model/          # File artefak/bobot model Linear Regression yang telah dilatih
├── notebook.ipynb  # Eksplorasi data (EDA), pra-pemrosesan, dan pelatihan model
├── main.py         # Aplikasi antarmuka interaktif berbasis Streamlit
├── .gitignore      # Daftar file/folder yang dikecualikan dari Git
└── README.md       # Dokumentasi proyek
```

---

## 📝 Catatan Tambahan

Proyek ini dibuat pada tahun **2021** sebagai bentuk eksperimen awal pemodelan *machine learning* sederhana. Umpan balik maupun kontribusi untuk pengembangan model lebih lanjut sangat diperbolehkan!