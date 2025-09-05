# pages/2_🧠_LSTM_Implementation.py

import streamlit as st
# from sklearn.metrics import classification_report
# import pandas as pd
# import time

# from src.data.data_loader import load_data
# from src.data.data_processing import oversample_data, prepare_data_for_model
from src.models.lstm_model import (
    # create_and_fit_tokenizer, build_lstm_model, texts_to_padded_sequences,
    # save_artifacts, load_artifacts, predict_sentiment_lstm
    load_lstm_model, predict_sentiment_lstm
)

@st.cache_resource
def get_lstm_model_and_tokenizer():
    return load_lstm_model()

st.set_page_config(page_title="LSTM Model", layout="wide")
st.title("🧠 Implementasi dengan LSTM")

st.markdown("""
Halaman ini menggunakan model **Long Short-Term Memory (LSTM)** yang telah di-*fine-tuning* pada dataset ulasan produk Amazon. 
Model ini akan diunduh dan di-cache saat pertama kali digunakan.
""")

# --- Bagian Prediksi ---
with st.spinner("Memuat model LSTM... Ini mungkin memerlukan beberapa saat pada saat pertama kali."):
    model, tokenizer = get_lstm_model_and_tokenizer()
    
if model and tokenizer:
    st.success("Model LSTM berhasil dimuat!")
    st.header("Coba Model LSTM")
    st.write("Masukkan teks ulasan di bawah ini untuk memprediksi sentimennya menggunakan model yang telah dilatih.")
    
    user_input = st.text_area("Tulis ulasan produk di sini:", "This product is amazing, I really love it!")
    if st.button("Prediksi Sentimen (LSTM)"):
        if user_input:
            with st.spinner("Menganalisis..."):
                prediction = predict_sentiment_lstm(user_input, model, tokenizer)
                if prediction == "Positive":
                    st.success(f"Analisis sentimen dari kalimat tersebut yaitu **{prediction}** 😊")
                else:
                    st.error(f"Analisis sentimen dari kalimat tersebut yaitu **{prediction}** 😞")
        else:
            st.warning("Mohon masukkan teks ulasan.")