import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils.config import config
from src.data.data_loader import DataLoader
from src.data.data_processing import DataProcessing

def dataset_overview():
    st.set_page_config(page_title=config.get("PAGE_DATASET_TITLE"), layout=config.get("LAYOUT_DATASET"))
    st.title("📊 Dataset Overview")

    data_loader = DataLoader()
    data_processing = DataProcessing()

    st.markdown("""
        The dataset used for *fine-tuning* the model is the Amazon Product dataset from 
        <a href="https://www.kaggle.com/datasets/mahmudulhaqueshawon/amazon-product-reviews/data" target="_blank">Kaggle</a>
    """, unsafe_allow_html=True)

    df_original = data_loader.load_data()

    if df_original is not None:
        st.markdown("---")
        st.subheader("1. Initial Data 📋")
        st.info("These are the first 5 lines of the original dataset:")
        st.dataframe(df_original.head())
        st.success(f"Initial data amount: **{df_original.shape[0]}** rows and {df_original.shape[1]} columns.")
    
        st.markdown("---")
        st.subheader("2. Initial Data Distribution 📉")
        st.write("The following is the sentiment distribution (Positive vs. Negative) before class balancing.")
    
        fig1, ax1 = plt.subplots(figsize=(15, 6))
        sns.set_style('whitegrid')
        sns.countplot(x='rating', data=df_original, palette='YlGnBu_r', hue='rating')
        ax1.set_title("Initial Data Distribution", fontsize=16)
        st.pyplot(fig1)

        st.markdown("---")
        st.subheader("3. Data Balancing with Oversampling Techniques ⚖️")
        st.write("""
        <div style="text-align: justify; margin-bottom: 20px;">
            Based on the previous image, we can see an imbalance in the data, where the number of reviews with positive labels 
            is much higher than the number of reviews with negative labels. To address this issue, we use the *Random Oversampling* 
            technique, technique to balance the class distribution. This is to prevent the model from predicting the majority class (positive label), 
            which can cause the model to become biased and less accurate in predicting the minority class.
        """, unsafe_allow_html=True)
    
        with st.spinner("⏳ Melakukan oversampling..."):
            df_resampled = data_processing.oversample_data(df_original)
    
        st.success(f"The amount of data after oversampling: **{df_resampled.shape[0]}** baris.")
        fig2, ax2 = plt.subplots(figsize=(15, 6))
        sns.set_style('whitegrid')
        sns.countplot(x='rating', data=df_resampled, palette='YlGnBu_r', hue='rating')
        ax2.set_title("Class Distribution After Oversampling", fontsize=16)
        st.pyplot(fig2)

        st.markdown("---")
        st.subheader("4. Sample Text After Pre-processing 🧼")
        st.info("The review text is cleaned by removing punctuation marks, converting to lowercase, and removing *stopwords*.")
    
        sample_text = df_resampled['text'].iloc[0]
        cleaned_text = data_processing.preprocess_text(sample_text)

        st.markdown(f"""
        <div style="background-color: #2e2e2e; padding: 15px; border-radius: 8px; margin-bottom: 10px;">
            <p><b>Original Text:</b></p>
            <p style="font-style: italic;">{sample_text}</p>
        </div>
        """, unsafe_allow_html=True)
    
        st.markdown(f"""
        <div style="background-color: #2e2e2e; padding: 15px; border-radius: 8px;">
            <p><b>Clean Text:</b></p>
            <p style="color: #90EE90; font-style: italic;">{cleaned_text}</p>
        </div>
        """, unsafe_allow_html=True)