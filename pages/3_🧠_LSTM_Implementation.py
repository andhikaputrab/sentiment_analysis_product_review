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
    load_lstm_model_huggingface, predict_sentiment_lstm
)

@st.cache_resource
def get_lstm_model_and_tokenizer(HF_TOKEN):
    return load_lstm_model_huggingface(HF_TOKEN)

st.set_page_config(page_title="LSTM Model", layout="wide")
st.title("🧠 Implementasi dengan LSTM")

st.markdown("""
Halaman ini menggunakan model **Long Short-Term Memory (LSTM)** yang telah di-*fine-tuning* pada dataset ulasan produk Amazon. 
Model ini akan diunduh dan di-cache saat pertama kali digunakan.
""")

# --- Input Hugging Face Token ---
st.subheader("🔐 Masukkan Hugging Face Token")
hf_token = st.text_input("Hugging Face Token", type="password", help="Masukkan token akses dari https://huggingface.co/settings/tokens")

# --- Bagian Prediksi ---
if not hf_token:
    st.info("Silakan masukkan Hugging Face token untuk melanjutkan.")
else:
    # --- Memuat Model ---
    with st.spinner("Memuat model LSTM dari Hugging Face... Ini mungkin memerlukan beberapa saat saat pertama kali."):
        try:
            model, tokenizer = get_lstm_model_and_tokenizer(hf_token)
            st.success("Model LSTM berhasil dimuat! 🎉")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memuat model: {e}")
            st.stop()

    # --- Bagian Prediksi ---
    st.header("💬 Coba Model LSTM")
    st.write("Masukkan teks ulasan di bawah ini untuk memprediksi sentimennya menggunakan model yang telah dilatih.")

    user_input = st.text_area(
        "Tulis ulasan produk di sini:",
        value="This product is amazing, I really love it!"
    )

    if st.button("🔍 Prediksi Sentimen (LSTM)"):
        if user_input.strip():
            with st.spinner("Menganalisis..."):
                try:
                    prediction = predict_sentiment_lstm(user_input, model, tokenizer)
                    if prediction == "Positive":
                        st.success(f"Analisis sentimen: **{prediction}** 😊")
                    else:
                        st.error(f"Analisis sentimen: **{prediction}** 😞")
                except Exception as e:
                    st.error(f"Error saat melakukan prediksi: {e}")
        else:
            st.warning("Mohon masukkan teks ulasan.")