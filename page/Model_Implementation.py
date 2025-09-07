import streamlit as st
from src.models.LSTM_Implementation import lstm_implementation
from src.models.DistilBERT_Implementation import distibert_implementation
from src.utils.styling import load_css
from src.utils.config import config

def model_implementation():
    load_css()

    st.set_page_config(
        page_title=config.get("PAGE_IMPLEMENTATION_TITLE"),
        page_icon=config.get("PAGE_IMPLEMENTATION_ICON"),
        layout=config.get("LAYOUT_IMPLEMENTATION"))

    st.title("Implementation of Sentiment Analysis Models")
    with st.spinner("Loading the model... This may take a few moments the first time."):
        st.markdown("""
            This page allows you to try two different models for sentiment analysis: **LSTM** and **DistilBERT**. 
            Use the tabs below to switch between them.
        """)

        # Create tabs
        tab1, tab2 = st.tabs(["🧠 Implementation with LSTM", "🤖 Implementation with DistilBERT"])

        with tab1:
            lstm_implementation()

        with tab2:
            distibert_implementation()