import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split
import pandas as pd
import streamlit as st

class DataProcessing:
    @staticmethod
    def download_nltk_resources():
        nltk.download('stopwords')
        nltk.download('punkt')

    @staticmethod
    @st.cache_data
    def preprocess_text(text):
        """Membersihkan dan memproses teks input."""
        DataProcessing.download_nltk_resources()
        stop_words = set(stopwords.words('english'))
    
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text)
        text = text.lower()
        words = word_tokenize(text)
        words = [word for word in words if word not in stop_words]
        return ' '.join(words)

    @staticmethod
    @st.cache_data
    def oversample_data(df):
        """Melakukan oversampling pada data untuk menyeimbangkan kelas."""
        X = df['Text'].values.reshape(-1, 1)
        y = df['label']
    
        oversampler = RandomOverSampler(random_state=42)
        X_resampled, y_resampled = oversampler.fit_resample(X, y)
    
        df_resampled = pd.DataFrame({'text': X_resampled.flatten(), 'label': y_resampled})
        df_resampled['rating'] = df_resampled['label'].apply(lambda x: 'Positive' if x == 1 else 'Negative')
        return df_resampled

    @staticmethod
    def prepare_data_for_model(df):
        """Membersihkan teks dan membagi data menjadi train dan test set."""
        df['clean_text'] = df['text'].apply(DataProcessing.preprocess_text)
    
        X = df['clean_text'].values
        y = df['label'].values
    
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test