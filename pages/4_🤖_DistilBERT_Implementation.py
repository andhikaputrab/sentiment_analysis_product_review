import streamlit as st
from src.models.bert_model import load_bert_model_and_tokenizer, analyze_sentiment_bert

st.set_page_config(page_title="DistilBERT Model", layout="wide")
st.title("🤖 Implementasi dengan DistilBERT")

st.markdown("""
Halaman ini menggunakan model **DistilBERT** yang telah di-*fine-tuning* pada dataset ulasan produk Amazon dan di-host pada [Hugging Face Hub](https://huggingface.co/andhikaputrab/distilbert-base-uncased-finetuned-product-review). 
Model ini akan diunduh dan di-cache saat pertama kali digunakan.
""")

# Load model saat aplikasi dimulai
with st.spinner("Memuat model DistilBERT... Ini mungkin memerlukan beberapa saat pada saat pertama kali."):
    model, tokenizer = load_bert_model_and_tokenizer()

if model and tokenizer:
    st.success("Model DistilBERT berhasil dimuat!")
    st.header("Coba Model DistilBERT")
    st.write("Masukkan teks ulasan di bawah ini dalam bahasa inggris untuk memprediksi sentimennya.")
    
    user_input = st.text_area("Tulis ulasan produk di sini:", "The quality is not as good as I expected.")
    
    if st.button("Prediksi Sentimen (DistilBERT)"):
        if user_input:
            with st.spinner("Menganalisis..."):
                prediction = analyze_sentiment_bert(user_input, model, tokenizer)
                if prediction == "Positive":
                    st.success(f"Analisis sentimen dari kalimat tersebut yaitu **{prediction}** 😊")
                else:
                    st.error(f"Analisis sentimen dari kalimat tersebut yaitu **{prediction}** 😞")
        else:
            st.warning("Mohon masukkan teks ulasan.")
else:
    st.error("Gagal memuat model DistilBERT. Silakan periksa koneksi internet Anda atau nama model di Hugging Face Hub.")