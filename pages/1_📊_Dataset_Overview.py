# pages/1_📊_Dataset_Overview.py

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils.config import config
from src.data.data_loader import DataLoader
from src.data.data_processing import DataProcessing

st.set_page_config(page_title="Dataset Overview", layout="wide")
st.title("📊 Tinjauan Dataset Ulasan Produk Amazon")

data_loader = DataLoader()
data_processing = DataProcessing()

# Load data
df_original = data_loader.load_data()

st.markdown("""
Dataset yang digunakan untuk fine-tuning model yaitu dataset Amazon Product dari [Kaggle](https://www.kaggle.com/datasets/mahmudulhaqueshawon/amazon-product-reviews/data)
""")

if df_original is not None:
    st.header("1. Data Awal")
    st.write("Berikut adalah 5 baris pertama dari dataset asli:")
    st.dataframe(df_original.head())
    st.write(f"Jumlah data awal: **{df_original.shape[0]}** baris.")

    # Visualisasi distribusi kelas awal
    st.header("2. Distribusi Sentimen Awal")
    st.write("Distribusi sentimen (Positive vs. Negative) sebelum penyeimbangan kelas.")
    
    fig1, ax1 = plt.subplots(figsize=(15, 6))
    sns.set_style('whitegrid')
    sns.countplot(x='rating', data=df_original, palette='YlGnBu_r', hue='rating')
    ax1.set_title("Distribusi Kelas Sebelum Oversampling")
    st.pyplot(fig1)

    # Oversampling dan visualisasi setelahnya
    st.header("3. Penyeimbangan Data dengan Oversampling")
    st.write("Dataset tidak seimbang, di mana satu kelas memiliki lebih banyak sampel daripada yang lain. Kami menggunakan teknik *Random Oversampling* untuk menyeimbangkan distribusi kelas.")
    
    with st.spinner("Melakukan oversampling..."):
        df_resampled = data_processing.oversample_data(df_original)
    
    st.write(f"Jumlah data setelah oversampling: **{df_resampled.shape[0]}** baris.")
    fig2, ax2 = plt.subplots(figsize=(15, 6))
    sns.set_style('whitegrid')
    sns.countplot(x='rating', data=df_resampled, palette='YlGnBu_r', hue='rating')
    ax2.set_title("Distribusi Kelas Setelah Oversampling")
    st.pyplot(fig2)

    st.header("4. Contoh Teks Setelah Pra-pemrosesan")
    st.write("Teks ulasan dibersihkan dengan menghilangkan tanda baca, mengubah ke huruf kecil, dan menghapus *stopwords*.")
    
    sample_text = df_resampled['text'].iloc[0]
    cleaned_text = data_processing.preprocess_text(sample_text)

    st.markdown(f"""
    **Teks Asli:**
    > {sample_text}

    **Teks Bersih:**
    > {cleaned_text}
    """)