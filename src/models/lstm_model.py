import tensorflow as tf
import streamlit as st
import pickle
import os
import shutil
# from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from huggingface_hub import hf_hub_download, login
from src.utils.logger import default_logger as logger
from src.utils.config import config
from dotenv import load_dotenv

MAX_WORDS = 5000
MAX_LEN = 128

load_dotenv()

@st.cache_resource
def login_huggingface(HF_TOKEN):
    # HF_TOKEN = os.getenv("HF_TOKEN")
    try:
        login(HF_TOKEN)
        print("Hugging Face login successful.")
        logger.info("Hugging Face login successful.")
    except Exception as e:
        print(f"Hugging Face login failed: {e}")
        logger.info(f"Hugging Face login failed: {e}")
        
# def create_and_fit_tokenizer(texts):
#     """Membuat dan melatih tokenizer pada teks."""
#     tokenizer = Tokenizer(num_words=MAX_WORDS)
#     tokenizer.fit_on_texts(texts)
#     return tokenizer

def texts_to_padded_sequences(texts, tokenizer):
    """Mengubah teks menjadi sequence yang di-padding."""
    sequences = tokenizer.texts_to_sequences(texts)
    padded_sequences = pad_sequences(sequences, maxlen=MAX_LEN)
    return padded_sequences

# def build_lstm_model(tokenizer):
#     """Membangun arsitektur model LSTM."""
#     model = tf.keras.models.Sequential([
#         tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=100, input_length=MAX_LEN),
#         tf.keras.layers.LSTM(64, return_sequences=False),
#         tf.keras.layers.Dropout(0.5),
#         tf.keras.layers.Dense(1, activation='sigmoid')
#     ])
    
#     model.compile(
#         optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
#         loss='binary_crossentropy',
#         metrics=['accuracy']
#     )
#     return model

# def save_artifacts(model, tokenizer, directory="artifacts/lstm"):
#     """Menyimpan model dan tokenizer yang telah dilatih."""
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     model.save(os.path.join(directory, "model.h5"))
#     with open(os.path.join(directory, "tokenizer.pkl"), "wb") as f:
#         pickle.dump(tokenizer, f)

# def load_artifacts(directory="artifacts/lstm"):
#     """Memuat model dan tokenizer yang sudah disimpan."""
#     model_path = os.path.join(directory, "model.h5")
#     tokenizer_path = os.path.join(directory, "tokenizer.pkl")
    
#     if not os.path.exists(model_path) or not os.path.exists(tokenizer_path):
#         return None, None
        
#     model = tf.keras.models.load_model(model_path)
#     with open(tokenizer_path, "rb") as f:
#         tokenizer = pickle.load(f)
#     return model, tokenizer

def load_lstm_model_huggingface(HF_TOKEN):
    try:
        login_huggingface(HF_TOKEN)
    
        # model_path = hf_hub_download(repo_id=config.get("HF_LSTM_MODEL"), filename="sentiment_lstm_model.h5")
        # tokenizer_path = hf_hub_download(repo_id=config.get("HF_LSTM_MODEL"), filename="tokenizer.pickle")
        
        # local_model_path = "artifacts/sentiment_lstm_model_local.h5"
        # local_tokenizer_path = "artifacts/tokenizer_local.pickle"
        
        # shutil.copy2(model_path, local_model_path)
        # shutil.copy2(tokenizer_path, local_tokenizer_path)
        
        model_path = config.get('LSTM_MODEL')
        tokenizer_path = config.get('LSTM_TOKENIZER')

        lstm_model = tf.keras.models.load_model(model_path)
        with open(tokenizer_path, 'rb') as f:
            tokenizer = pickle.load(f)
            
        print("Berhasil memuat LSTM model dari Hugging Face Hub")
        logger.info("Berhasil memuat LSTM model dari Hugging Face Hub")
        return lstm_model, tokenizer
    except Exception as e:
        print(f"Gagal memuat LSTM model dari Hugging Face Hub: {e}")
        logger.info(f"Gagal memuat LSTM model dari Hugging Face Hub: {e}")
        return None, None

def predict_sentiment_lstm(text, model, tokenizer):
    """Memprediksi sentimen dari satu teks menggunakan model LSTM."""
    try:
        processed_text = texts_to_padded_sequences([text], tokenizer)
        prediction = model.predict(processed_text)
        return "Positive" if prediction[0][0] >= 0.5 else "Negative"
    except Exception as e:
        print(f"Gagal melakukan analisis sentimen: {e}")
        logger.info(f"Gagal melakukan analisis sentimen: {e}")
        return "Error"