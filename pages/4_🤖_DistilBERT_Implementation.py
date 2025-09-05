import streamlit as st
from src.models.bert_model import load_bert_model_and_tokenizer, analyze_sentiment_bert

@st.cache_resource
def get_distilbert_model_and_tokenizer(HF_TOKEN):
    return load_bert_model_and_tokenizer(HF_TOKEN)

st.set_page_config(page_title="DistilBERT Model", layout="wide")
st.title("🤖 Implementasi dengan DistilBERT")

st.markdown("""
Halaman ini menggunakan model **DistilBERT** yang telah di-*fine-tuning* pada dataset ulasan produk Amazon dan di-host pada [Hugging Face Hub](https://huggingface.co/andhikaputrab/distilbert-base-uncased-finetuned-product-review). 
Model ini akan diunduh dan di-cache saat pertama kali digunakan.
""")

# --- Input Hugging Face Token ---
st.subheader("🔐 Masukkan Hugging Face Token")
hf_token = st.text_input("Hugging Face Token", type="password", help="Masukkan token akses dari https://huggingface.co/settings/tokens")

# Load model saat aplikasi dimulai
if not hf_token:
    st.info("Silakan masukkan Hugging Face token untuk melanjutkan.")
else:
    # --- Memuat Model ---
    with st.spinner("Memuat model LSTM dari Hugging Face... Ini mungkin memerlukan beberapa saat saat pertama kali."):
        try:
            model, tokenizer = get_distilbert_model_and_tokenizer(hf_token)
            st.success("Model LSTM berhasil dimuat! 🎉")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memuat model: {e}")
            st.stop()
            
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