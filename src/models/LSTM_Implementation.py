import streamlit as st
from src.models.lstm_model import load_lstm_model, predict_sentiment_lstm

@st.cache_resource
def get_lstm_model_and_tokenizer():
    return load_lstm_model()

def lstm_implementation():
    st.markdown("""
    <div class="model-info">
        This page uses a <strong>Long Short-Term Memory (LSTM)</strong> model that has been fine-tuned on Amazon product review datasets. 
        This model will be downloaded and cached the first time it is used.
    </div>
    """, unsafe_allow_html=True)

    # Informasi model
    with st.expander("ℹ️ LSTM Model Information", expanded=True):
        st.markdown("""
        - **Architecture**: LSTM with embedding layer and dense layer
        - **Training**: Trained on Amazon product review dataset
        - **Accuracy**: Achieved 94% accuracy on testing data
        """)

    # --- Bagian Prediksi ---
    with st.spinner("Memuat model LSTM... Ini mungkin memerlukan beberapa saat pada saat pertama kali."):
        model, tokenizer = get_lstm_model_and_tokenizer()
    
    if model and tokenizer:
        st.success("✅ The LSTM model was successfully loaded.!")
    
        st.markdown("""
        <div class="section-header">
            <h2>🔮 Try the LSTM Model</h2>
        </div>
        """, unsafe_allow_html=True)
    
        st.write("Enter the review text below in English to predict its sentiment.")
    
        # Input teks
        user_input = st.text_area(
            "Write a product review here:", 
            "This product is amazing, I really love it!",
            height=100
        )
    
        # Tombol prediksi
        if st.button("🎯 Sentiment Prediction (LSTM)", type="primary"):
            if user_input:
                with st.spinner("Analyzing..."):
                    prediction = predict_sentiment_lstm(user_input, model, tokenizer)
                
                    # Tampilkan hasil dengan visual yang menarik
                    if prediction == "Positive":
                        st.markdown(f"""
                        <div class="prediction-positive">
                            <h2>😊 Positive Sentiment</h2>
                            <p>The sentiment analysis of the sentence is <strong>{prediction}</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="prediction-negative">
                            <h2>😞 Negative Sentiment</h2>
                            <p>The sentiment analysis of the sentence is <strong>{prediction}</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.warning("⚠️ Please enter your review text.")