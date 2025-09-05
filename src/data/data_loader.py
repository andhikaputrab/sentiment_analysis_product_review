import pandas as pd
import streamlit as st
from typing import Optional
from src.utils.logger import default_logger as logger
from src.utils.config import config

class DataLoader:
    def __init__(self, data_path: Optional[str] = None):
        """
        initilize data loader

        Args:
            data_path: Optional path to data file
        """
        self.data_path = data_path or config.get('data_path')
        logger.info(f"initialized DataLoader with path: {self.data_path}")

    @st.cache_data # Cache data agar tidak di-load ulang setiap kali ada interaksi
    def load_data(_self):
        """
        Memuat data dari file CSV, menghapus baris kosong, 
        dan menambahkan kolom 'rating'.
        """
        try:
            df = pd.read_csv(_self.data_path)
            df.dropna(inplace=True)
            df['rating'] = df['label'].apply(lambda x: 'Positive' if x == 1 else 'Negative')
            logger.info(f"loaded data successfully with shape {df.shape}")
            return df
        except Exception as e:
            st.error(f"File tidak ditemukan di path: {self.data_path}")
            logger.info(f"Error loading data: {e}")
            return None