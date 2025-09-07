import streamlit as st

def load_css():
    with open('static/css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# def load_css():
#     st.markdown("""
#     <style>
#     /* Global Styles */
#     .main-header {
#         background: linear-gradient(135deg, #6e8efb, #a777e3);
#         padding: 2rem;
#         border-radius: 10px;
#         color: white;
#         margin-bottom: 2rem;
#         text-align: center;
#     }
    
#     .main-header h1 {
#         font-size: 2.5rem;
#         margin-bottom: 0.5rem;
#     }
    
#     .main-header p {
#         font-size: 1.2rem;
#         opacity: 0.9;
#     }
    
#     /* Welcome Page Styles */
#     .welcome-container {
#         display: flex;
#         justify-content: space-between;
#         gap: 1rem;
#         margin-bottom: 2rem;
#     }
    
#     .welcome-card {
#         background: white;
#         padding: 1.5rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         flex: 1;
#         transition: transform 0.3s ease;
#     }
    
#     .welcome-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
#     }
    
#     .welcome-card h3 {
#         color: #6e8efb;
#         margin-bottom: 0.5rem;
#     }
    
#     .description-box {
#         background: #f8f9fa;
#         padding: 1.5rem;
#         border-radius: 10px;
#         border-left: 4px solid #6e8efb;
#     }
    
#     /* Card Styles */
#     .info-box {
#         background: #e3f2fd;
#         padding: 1rem;
#         border-radius: 10px;
#         margin-bottom: 2rem;
#         border-left: 4px solid #2196f3;
#     }
    
#     .section-header {
#         background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
#         padding: 1rem;
#         border-radius: 10px;
#         margin: 1.5rem 0;
#     }
    
#     .section-header h2 {
#         color: #2c3e50;
#         margin: 0;
#     }
    
#     /* Profile Styles */
#     .profile-image-container {
#         display: flex;
#         justify-content: center;
#         margin-bottom: 1.5rem;
#     }
    
#     .profile-image {
#         width: 200px;
#         height: 200px;
#         border-radius: 50%;
#         object-fit: cover;
#         border: 4px solid #6e8efb;
#     }
    
#     .contact-card {
#         background: white;
#         padding: 1.5rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         margin-bottom: 1.5rem;
#     }
    
#     .social-links {
#         display: flex;
#         justify-content: space-around;
#         margin-top: 1rem;
#     }
    
#     .social-links img {
#         width: 36px;
#         height: 36px;
#         transition: transform 0.3s ease;
#     }
    
#     .social-links img:hover {
#         transform: scale(1.1);
#     }
    
#     .profile-header h1 {
#         color: #2c3e50;
#         margin-bottom: 0.5rem;
#     }
    
#     .profile-header h2 {
#         color: #6e8efb;
#         margin-top: 0;
#     }
    
#     .summary-card {
#         background: #f8f9fa;
#         padding: 1.5rem;
#         border-radius: 10px;
#         margin: 1.5rem 0;
#         border-left: 4px solid #6e8efb;
#     }
    
#     .experience-card, .education-card, .certification-card {
#         background: white;
#         padding: 1.5rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         margin-bottom: 1.5rem;
#     }
    
#     .experience-header, .education-header, .certification-header {
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         margin-bottom: 1rem;
#     }
    
#     .experience-period, .education-period, .certification-period {
#         background: #6e8efb;
#         color: white;
#         padding: 0.3rem 0.8rem;
#         border-radius: 20px;
#         font-size: 0.8rem;
#     }
    
#     .skill-card {
#         background: white;
#         padding: 1.5rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         margin-bottom: 1.5rem;
#     }
    
#     .skill-card h3 {
#         color: #6e8efb;
#         margin-bottom: 1rem;
#     }
    
#     .skill-card ul {
#         list-style-type: none;
#         padding: 0;
#     }
    
#     .skill-card li {
#         padding: 0.5rem 0;
#         border-bottom: 1px solid #eee;
#     }
    
#     .skill-card li:last-child {
#         border-bottom: none;
#     }
    
#     /* Text Comparison */
#     .text-comparison {
#         display: flex;
#         gap: 1rem;
#         margin: 1.5rem 0;
#     }
    
#     .original-text, .cleaned-text {
#         flex: 1;
#         background: white;
#         padding: 1.5rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
    
#     .original-text h4, .cleaned-text h4 {
#         color: #2c3e50;
#         margin-bottom: 1rem;
#     }
    
#     .original-text blockquote, .cleaned-text blockquote {
#         background: #f8f9fa;
#         padding: 1rem;
#         border-left: 4px solid #6e8efb;
#         margin: 0;
#         font-style: italic;
#     }
    
#     /* Prediction Styles */
#     .model-info {
#         padding: 1rem;
#         border-radius: 10px;
#         margin-bottom: 2rem;
#         border-left: 4px solid #2196f3;
#         border-right: 4px solid #2196f3;
#     }
    
#     .prediction-positive {
#         background: linear-gradient(135deg, #4CAF50, #8BC34A);
#         padding: 2rem;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#         margin: 2rem 0;
#     }
    
#     .prediction-negative {
#         background: linear-gradient(135deg, #F44336, #FF9800);
#         padding: 2rem;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#         margin: 2rem 0;
#     }
    
#     /* Button Styles */
#     .download-button {
#         display: inline-block;
#         background: linear-gradient(135deg, #6e8efb, #a777e3);
#         color: white;
#         padding: 0.8rem 1.5rem;
#         border-radius: 30px;
#         text-decoration: none;
#         font-weight: bold;
#         margin: 1rem 0;
#         transition: all 0.3s ease;
#     }
    
#     .download-button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#         color: white;
#     }
    
#     /* Responsive Design */
#     @media (max-width: 768px) {
#         .welcome-container {
#             flex-direction: column;
#         }
        
#         .text-comparison {
#             flex-direction: column;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)