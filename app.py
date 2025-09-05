# app.py

import streamlit as st
from src.utils.styling import load_css

load_css()
st.title("🚀 Selamat Datang di Aplikasi Analisis Sentimen!")

st.markdown("""
Aplikasi ini dirancang untuk menganalisis sentimen dari ulasan produk Amazon dengan menggunakan model LSTM dan DistilBERT. 

**Fitur Aplikasi:**
- **📊 Dataset Overview**: Menampilkan visualisasi dan informasi dasar mengenai dataset yang digunakan.
- **🧠 LSTM Implementation**: Menggunakan model Long Short-Term Memory (LSTM) yang telah di-*fine-tuning* dan menggunakannya untuk prediksi.
- **🤖 DistilBERT Implementation**: Menggunakan model DistilBERT yang sudah di-*fine-tuning* dari Hugging Face Hub untuk analisis sentimen.

Silakan pilih halaman dari sidebar di sebelah kiri untuk memulai.
""")