import streamlit as st
from src.utils.styling import load_css
from src.utils.config import config
import base64

def get_pdf_download_link(pdf_path, filename):
    """Generate download link for PDF file"""
    with open(pdf_path, "rb") as f:
        bytes_data = f.read()
    b64 = base64.b64encode(bytes_data).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}" class="download-button">📥 Download CV</a>'
    return href

st.set_page_config(
    page_title=config.get('PAGE_TITLE_PROFILE'), 
    page_icon=config.get('PAGE_ICON_PROFILE'), 
    layout=config.get('LAYOUT_PROFILE')
)

load_css()

col1, col2 = st.columns([1, 2])

with col1:
    # Profile Image
    st.image("static/img/foto.jpg", width=200, output_format="auto")
    
    # Contact Information
    st.markdown("""
    ### Contact
    - 📧 andhikaputra1301@gmail.com
    - 📱 082213676520 (WA)
    - [![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/andhika-putra-bagaskara13/) | [![Instagram](https://img.icons8.com/color/48/000000/github.png)](https://github.com/andhikaputrab) | [![Instagram](https://img.icons8.com/color/48/000000/instagram-new--v1.png)](https://www.instagram.com/andhikaputrab/)
    """)
    
with col2:
    st.title("Andhika Putra Bagaskara")
    st.subheader("Data Analyst")
    st.markdown(get_pdf_download_link("cv/CV ATS - Andhika Putra Bagaskara.pdf", "cv_andhika_putra_bagaskara.pdf"), unsafe_allow_html=True)
    
    st.markdown("""
    ### Summary
    <div style="text-align: justify;">I am a Bachelor Degree of Informatics Engineering and currently attending Master Degree of Informatics Engineering on Telkom University.
    Proficiency in data processing, visualization, Python, Machine Learning, Tableau, and Excel. Good problem-solving and critical thinking skills, committed to providing accurate data insights to support company 
    decision-making, and highly motivated to continue learning and developing in the field of data analytics.</div>
    """, unsafe_allow_html=True)
    
# Experience Section
st.header("Working Experience")

experiences = [
    {
        "role": "Internship",
        "company": "PT Pertamina Persero",
        "period": "October 2022 - October 2023",
        "points": [
            "Automate the management of ticket request data from the website using UiPath and send the analysisvia email to the relevant department.",
            "Developing a website application for asset management for internal functions using CodeIgniter, MySQL,JavaScript, and HTML",
        ]
    }
]

for exp in experiences:
    with st.expander(f"**{exp['company']} - {exp['role']}**", expanded=True):
        st.markdown(f"**Period:** {exp['period']}")
        for point in exp['points']:
            st.markdown(f"- {point}")
            
# Skill Section
st.header("Skill & Expertise")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Technical Skills")
    technical_skills = [
        "Machine Learning",
        "Data Analysis",
        "Python Programming",
        "SQL",
        "Data Visualization",
    ]
    for skill in technical_skills:
        st.markdown(f"- {skill}")

with col2:
    st.subheader("Soft Skill")
    soft_skill = [
        "Communication",
        "Problem Solving",
        "Analytical Thinking",
        "Teamwork"
    ]
    for tool in soft_skill:
        st.markdown(f"- {tool}")

# Education Section
st.header("Education")
education = [
    {
        "university": "Telkom University",
        "period": " 2024 - Present ",
        "degree": "Master Degree of Informatics Engineering",
        "coursework": "Data Analysis, Machine Learning, Artificial Intelligence, Natural Language Processing",
        "GPA": "3.26/4.00",
    },
    {
        "university": "Universitas Komputer Indonesia",
        "period": "2017 - 2022",
        "degree": "Bachelor Degree of Informatics Engineering",
        "coursework": "Software Engineering, Artificial Intelligence, Mobile Programming, Web Programming",
        "GPA": "3.07/4.00",
    }
]

for edu in education:
    with st.expander(f"**{edu['university']} ({edu['period']})**", expanded=True):
        st.markdown(f" {edu['degree']}")
        st.markdown(f" **Relevant Coursework:** {edu['coursework']}")
        st.markdown(f" **GPA:** {edu['GPA']}")

# # Certifications
# st.header("Certifications")
# st.markdown("""
# #### Big Data using Python
# - **orginizer:** Online Course – Kominfo
# - **Relevant Coursework:** Python, Data Analysis, Data Cleaning
# - **Period:** 2021
# """)
# st.markdown("""
# #### Google Data Analytics
# - **orginizer:** Online Course – Kominfo
# - **Relevant Coursework:** Python, Data Analysis, Data Cleaning, Tableau
# - **Period:** 2024
# """)
# st.markdown("""
# #### English Proficiency Test (EPRT)
# - **orginizer:** Telkom University
# - **Period:** 2025
# - **Score:** 513
# """)

st.header("Certifications")

certifications = [
    {
        "title": "Big Data using Python",
        "orginizer": "Online Course – Kominfo",
        "Relevant Course": "Data Processing, Data Visualization, Python",
        "period": "2021"
    },
    {
        "title": "Google Data Analytics",
        "orginizer": "Online Course – Kominfo",
        "Relevant Course": "Data Processing, Data Visualization, Python, R, Tableau",
        "period": "2024"
    },
    {
        "title": "English Proficiency Test (EPRT)",
        "orginizer": "Telkom University",
        "period": "2025"
    }
]
    
for cert in certifications:
    with st.expander(f"**{cert['title']} ({cert['period']})**", expanded=True):
        st.markdown(f"{cert['orginizer']}")
        if cert['title'] == "English Proficiency Test (EPRT)":
            st.markdown("Score: 513")
        else:
            st.markdown(f"**Relevant Course:** {cert['Relevant Course']}")
        
