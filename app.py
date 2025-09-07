import streamlit as st
from src.utils.styling import load_css
from src.utils.config import config
from page.Dataset_Overview import dataset_overview
from page.Profile import profile
from page.Model_Implementation import model_implementation

load_css() # Memuat file CSS kustom untuk styling

def Home():
    st.sidebar.markdown("---")

    st.title("🚀 Welcome to the Sentiment Analysis Application!")

    st.markdown("""
    This application is designed to analyze sentiment from Amazon product reviews using **LSTM** and **DistilBERT** models. 

    ---
    """)

    st.subheader("🌟 Main Features")

    st.markdown("""
    <div style="background-color: #2e2e2e; padding: 20px; border-radius: 10px; margin-bottom: 15px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
        <h4 style="color: #4CAF50;">📊 Dataset Overview</h4>
        <p>View visualizations and basic information about the Amazon product review dataset used.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #2e2e2e; padding: 20px; border-radius: 10px; margin-bottom: 15px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
        <h4 style="color: #4CAF50;">🧠 Implementasi dengan LSTM</h4>
        <p>Try the Long Short-Term Memory (LSTM) model that has been trained to predict sentiment from review text.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #2e2e2e; padding: 20px; border-radius: 10px; margin-bottom: 15px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
        <h4 style="color: #4CAF50;">🤖 Implementasi dengan DistilBERT</h4>
        <p>Use the fine-tuned DistilBERT model for more advanced sentiment analysis.</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Silakan pilih halaman dari sidebar di sebelah kiri untuk memulai eksplorasi. 😊")

# --- Sidebar ---
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #4CAF50;">Portofolio</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")
st.sidebar.image("static/img/sentiment_icon.png", use_container_width=True)

# Navigation radio buttons
page = st.sidebar.radio(
    "Pilih Halaman",
    ["Home", "Profile", "Dataset Overview", "Model Implementation"],
)

if page == "Home":
    Home()
elif page == "Profile":
    profile()
elif page == "Dataset Overview":
    dataset_overview()
elif page == "Model Implementation":
    model_implementation()