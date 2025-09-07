import streamlit as st
from src.models.bert_model import load_bert_model_and_tokenizer, analyze_sentiment_bert

def distibert_implementation():

    st.markdown("""
    <div class="model-info">
        This page uses the <strong>DistilBERT</strong> model, which has been fine-tuned on Amazon product review datasets 
        and hosted on the <a href="https://huggingface.co/andhikaputrab/distilbert-base-uncased-finetuned-product-review" target="_blank">Hugging Face Hub</a>. 
        This model will be downloaded and cached the first time it is used.
    </div>
    """, unsafe_allow_html=True)

    # Informasi model
    with st.expander("ℹ️ DistilBERT Model Information", expanded=True):
        st.markdown("""
        - **Architecture**: DistilBERT (a simplified version of BERT)
        - **Training**: Fine-tuned on Amazon product review datasets
        - **Accuracy**: Achieved 95% accuracy in testing data
        - **Advantages**: Faster and more efficient than BERT with nearly equivalent performance
    """)

    # Load model saat aplikasi dimulai
    with st.spinner("Loading the DistilBERT model... This may take a few moments the first time."):
        model, tokenizer = load_bert_model_and_tokenizer()

    if model and tokenizer:
        st.success("✅ The DistilBERT model has been successfully loaded!")

        st.markdown("""
        <div class="section-header">
            <h2>🔮 Try the DistilBERT Model</h2>
        </div>
        """, unsafe_allow_html=True)

        st.write(
            "Enter the review text below in English to predict its sentiment.")

        # Input teks
        user_input = st.text_area(
            "Write a product review here:",
            "The quality is not as good as I expected.",
            height=100
        )

        # Tombol prediksi
        if st.button("🎯 Sentiment Prediction (DistilBERT)", type="primary"):
            if user_input:
                with st.spinner("Analyzing..."):
                    prediction = analyze_sentiment_bert(
                        user_input, model, tokenizer)

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
                st.warning("⚠️ Mohon masukkan teks ulasan.")
    else:
        st.error("❌ Failed to load the DistilBERT model. Please check your internet connection or the model name on Hugging Face Hub.")
