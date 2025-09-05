import torch
import streamlit as st
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
from huggingface_hub import login
from src.utils.logger import default_logger as logger
from src.utils.config import config

load_dotenv()

@st.cache_resource
def login_huggingface():
    # HF_TOKEN = os.getenv("HF_TOKEN")
    HF_TOKEN = st.secrets["HF_TOKEN"]
    try:
        login(HF_TOKEN)
        print("Hugging Face login successful.")
        logger.info("Hugging Face login successful.")
    except Exception as e:
        print(f"Hugging Face login failed: {e}")
        logger.info(f"Hugging Face login failed: {e}")
    

@st.cache_resource # Cache model agar tidak di-load ulang
def load_bert_model_and_tokenizer():
    """Memuat model dan tokenizer DistilBERT dari Hugging Face Hub."""
    login_huggingface()
    try:
        tokenizer = AutoTokenizer.from_pretrained(config.get("HF_BERT_MODEL"))
        model = AutoModelForSequenceClassification.from_pretrained(config.get("HF_BERT_MODEL"))
        logger.info("Berhasil memuat DistilBERT model dari Hugging Face Hub")
        return model, tokenizer
    except Exception as e:
        st.error(f"Gagal memuat model dari Hugging Face Hub: {e}")
        logger.info(f"Gagal memuat model dari Hugging Face Hub: {e}")
        return None, None

def analyze_sentiment_bert(text, model, tokenizer):
    """Menganalisis sentimen teks menggunakan model DistilBERT."""
    if not model or not tokenizer:
        return "Model tidak tersedia."
    
    try:
        inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
    
        prediction = torch.argmax(outputs.logits, dim=-1).item()
        logger.info("Berhasil melakukan analisis sentimen!")
        return model.config.id2label[prediction]
    except Exception as e:
        print(f"Gagal melakukan analisis sentimen: {e}")