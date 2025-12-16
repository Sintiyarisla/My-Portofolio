import streamlit as st
from typing import List, Dict
import os
import base64
import mimetypes
import textwrap
import urllib.parse

# Konfigurasi Halaman
st.set_page_config(page_title="Sintiya Risla", layout="wide")


# ============================
#   PREMIUM MODERN CSS
# ============================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
    --primary: #2E3A59; /* Biru Tua */
    --secondary: #5b6b7b;
    --muted: #8896a5;
    --bg: #f7f9fb;
    --card-bg: #ffffff;
    --radius: 12px;
    --accent: #2c9aff; /* Biru Aksen */
}

html, body {
    background: var(--bg);
    font-family: Inter, sans-serif;
}

/* Ensure anchors don't get underlined by host CSS after deploy */
a, a:link, a:visited, a:hover, a:active {
    text-decoration: none !important;
    color: inherit !important;
}

/* -------------------- */
/* 0. TOP FOOTER HERO */
/* -------------------- */
.footer-hero {
    background: linear-gradient(135deg, #243141 0%, #1f2a34 100%);
    color: #e8eef6;
    padding: 60px 20px;
    margin-top: 60px;
    border-radius: 10px;
    overflow: hidden;
}

.footer-hero-content {
    max-width: 1250px;
    margin: 0 auto;
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 40px;
}

.footer-hero-left h1 {
    font-size: 56px;
    font-weight: 800;
    color: #f5f8fb;
    margin: 0 0 12px 0;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.footer-contact-heading {
    color: #c7d4e2;
    font-size: 20px;
    margin-top: 18px;
    margin-bottom: 8px;
    font-weight: 600;
}

.footer-hero-left p,
.footer-hero-right p {
    font-size: 16px;
    color: #c1ccd8;
    margin: 0 0 6px 0;
    line-height: 1.6;
}

.footer-hero-right {
    margin-left: auto;
    text-align: left;
}

/* Social icons centered at bottom of footer-hero */
.footer-hero-socials {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 34px;
}
.social-icon {
    display: inline-block;
    width: 42px;
    height: 42px;
    line-height: 42px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.12);
    color: #e8eef6;
    text-align: center;
    font-weight: 700;
    text-decoration: none;
}
.social-icon:hover {
    background: rgba(255,255,255,0.04);
}

/* -------------------- */
/* 1. NAVBAR STYLING */
/* -------------------- */
.nav {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 2px solid #e5e9ef;
    padding: 16px 0;
}

.nav .container {
    max-width: 1250px;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 20px;
    gap: 30px;
}

.nav-links {
    display: flex;
    gap: 16px;
    align-items: center;
}

.nav-link {
    text-decoration: none;
    color: var(--secondary);
    font-weight: 600;
    padding: 10px 16px;
    border-radius: 8px;
    transition: all 0.3s ease;
    cursor: pointer;
    font-size: 15px;
}

.nav-link:hover {
    color: var(--primary);
    background-color: #f0f4f8;
}

.nav-link.active {
    color: var(--accent);
    border-bottom: 3px solid var(--accent);
    background: rgba(44, 154, 255, 0.08);
}

/* -------------------- */
/* 2. HERO & HEADINGS */
/* -------------------- */
.hero {
    max-width: 1250px;
    margin: 30px auto 20px auto;
    padding: 0 20px;
    display: flex;
    align-items: center;
    gap: 40px;
}

.hero h2 {
    font-size: 48px; 
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 0;
}

.hero h4 {
    font-size: 22px; 
    color: var(--accent); 
    margin-top: 4px; 
}

.hero p {
    font-size: 18px; 
    color: var(--muted);
    margin-top: 20px; 
    line-height: 1.7;
}

.hero img {
    width: 340px;
    border-radius: var(--radius);
    box-shadow: 0 8px 28px rgba(0,0,0,0.12);
}

/* Skill card improvements */
.skill-card {
    background: var(--card-bg);
    padding: 28px;
    border-radius: 16px;
    border: 1px solid #eef3f7;
    box-shadow: 0 10px 20px rgba(16,34,56,0.04);
}

.skill-card h4 { margin-top: 0; font-size: 26px; color: var(--primary); }


/* SECTIONS */
.section {
    max-width: 1250px;
    margin: 70px auto;
    padding: 0 28px;
}

h2 {
    color: var(--primary);
    font-weight: 700;
    border-left: 4px solid var(--accent);
    padding-left: 10px;
}

/* -------------------- */
/* 3. PROJECT CARDS */
/* -------------------- */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px 28px;
    margin-top: 32px;
    align-items: stretch;
    grid-auto-rows: 1fr;
}

.project {
    background: var(--card-bg);
    padding: 18px;
    border-radius: var(--radius);
    border: 1px solid #e8ecf1;
    transition: 0.25s ease;
    box-shadow: 0 6px 18px rgba(16,34,56,0.04);
    display: flex;
    flex-direction: column;
    min-height: 420px;
    height: 100%;
}

.project:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 28px rgba(0,0,0,0.08);
}

.project img {
    width: 100%;
    height: 200px;
    border-radius: 10px;
    object-fit: cover;
    display: block;
}

.project h3 {
    margin-top: 12px;
    font-size: 20px;
    margin-bottom: 6px;
}

.project-body {
    display: flex;
    flex-direction: column;
    gap: 10px;
    flex: 1 1 auto;
}

.project-desc {
    color: var(--secondary);
    font-size: 15px;
    line-height: 1.6;
    display: -webkit-box;
    -webkit-line-clamp: 5;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.project-footer {
    margin-top: auto;
}

@media (max-width: 1000px) {
    .projects-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 640px) {
    .projects-grid { grid-template-columns: repeat(1, 1fr); }
    .hero { flex-direction: column; gap: 18px; }
    .hero img { width: 280px; }
    .section { margin: 40px auto; }
}

.project a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
}

/* CTA link style */
.cta-link {
    display: inline-block;
    background: var(--accent);
    color: #fff !important;
    padding: 10px 16px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
}

/* -------------------- */
/* 5. BOTTOM FOOTER STYLING */
/* -------------------- */
.footer-dark {
    background: linear-gradient(135deg, #2E3A59 0%, #1f2a3a 100%);
    color: #d4dce3;
    padding: 60px 20px;
    margin-top: 100px;
    text-align: center;
}

.footer-dark p {
    margin: 4px 0;
    font-size: 14px;
    color: #b8c5d6;
}


/* -------------------- */
/* 5. STREAMLIT OVERRIDES */
/* -------------------- */
/* Menyembunyikan elemen Streamlit default untuk tampilan bersih */
[data-testid="stSidebar"] {
    display: none
}

[data-testid="stToolbar"] {
    right: 0px !important;
}

/* PROJECT FILTER */
.project-filters {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin: 18px 0 12px 0;
}

.filter-btn {
    padding: 8px 18px;
    border-radius: 20px;
    border: 1.5px solid rgba(44,154,255,0.25);
    background: transparent;
    color: var(--accent);
    font-weight: 600;
    cursor: pointer;
    transition: 0.2s ease;
    text-decoration: none;
}

.filter-btn.active {
    background: var(--accent);
    color: white;
    border-color: transparent;
}

.filter-btn:hover {
    background: rgba(44,154,255,0.06);
}

"""

st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


# ============================
#   COMPONENTS
# ============================

# Single-page layout: navigation removed (all content shown sequentially)



def hero(name: str, roles: str, tagline: str, image_url: str):
    st.markdown('<a id="home"></a>', unsafe_allow_html=True)

    st.markdown('<div class="hero">', unsafe_allow_html=True)

    left, right = st.columns([1.5, 1])

    with left:
        # Render headings and tagline; tagline uses HTML <strong> for bold phrase
        st.markdown(f"<h2 style='margin:0'>{name}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='margin:6px 0 12px 0;color:var(--accent)'>{roles}</h4>", unsafe_allow_html=True)
        # Tagline may include an emphasized phrase — ensure it renders bold by using <strong>
        st.markdown(f"<p style='color:var(--muted);font-size:18px;line-height:1.6'>{tagline}</p>", unsafe_allow_html=True)
        st.markdown('<div style="margin-top: 20px">', unsafe_allow_html=True)
        # Use a Streamlit button so the action works reliably
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.image(image_url, width=340)

    st.markdown("</div>", unsafe_allow_html=True)


def projects_section(projects: List[Dict]):
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("<h2>Featured Projects</h2>", unsafe_allow_html=True)
    
    # Build HTML for the grid to rely fully on our CSS grid (avoid mixing Streamlit columns)
    card_blocks = []
    for p in projects:
        link_html = f'<a href="{p.get("link")}" target="_blank">View Project &rarr;</a>' if p.get('link') else '<span style="color:var(--muted);font-size:14px;">(Internal Project)</span>'
        img_src = p.get('image', '')
        card = f'''
            <div class="project">
                <img src="{img_src}">
                <div class="project-body">
                    <h3 style="color:var(--primary);">{p.get('title','Untitled')}</h3>
                    <p class="project-desc">{p.get('description','')}</p>
                    <div class="project-footer">{link_html}</div>
                </div>
            </div>
        '''
        card_blocks.append(card)

    html = '<div class="projects-grid">' + '\n'.join(card_blocks) + '</div>'
    st.markdown(html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ============================
#   PAGES
# ============================

def render_home():
    hero(
        name="Sintiya Risla Miftaqul Nikmah",
        roles="Data Science Student | Mathematics & Statistics Tutor | Aspiring Data Scientist",
        tagline="Data Science student passionate about <strong>applied statistics, data visualization, and machine learning</strong>.",
        image_url="me.png"
    )

    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.markdown("---")

def render_about():
    st.markdown('<a id="about"></a>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("<h2>About Me</h2>", unsafe_allow_html=True)
    
    left_col, right_col = st.columns([5, 0.5])

    with left_col:
        st.markdown("""
        <p style='font-size: 18px; color: var(--secondary); line-height: 1.7;'>
        I am a Data Science student with a strong interest in data analysis, applied statistics, and machine learning. I have experience as a mathematics and statistics tutor and have been actively involved in scientific writing and data-related competitions, which have strengthened my analytical and problem-solving skills.</p>
        <p style='font-size: 18px; color: var(--secondary); line-height: 1.7;'>
        I am continuously developing my technical abilities through coursework, internships, and self-directed learning, with hands-on experience in data collection, analysis, and visualization. I enjoy identifying patterns, predicting trends, and communicating insights using tools such as Python, R, Excel, Tableau, PHP, and CSS, and I am motivated to contribute to impactful, data-driven projects.</p>
        <p style='margin-top:14px'>
        <a class='cta-link' href='https://drive.google.com/file/d/1sqTBzOJwMZYddfkS8DG8hUJ-phwqjRjk/view?usp=sharing' target='_blank'>View Full CV</a>
        </p>
        """, unsafe_allow_html=True)

    st.markdown("---")


    st.markdown("<h2>Expertise Snapshot</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div style="background-color: var(--card-bg); padding: 20px; border-radius: var(--radius); border-left: 5px solid var(--accent);">
                <h4 style="color: var(--primary); margin-top: 0;">Data Visualization</h4>
                <p style="font-size: 15px; color: var(--muted); margin-bottom: 0;">Skilled in transforming complex data into clear and insightful visualizations, including interactive dashboards and statistical graphics using Tableau, Streamlit, and Python visualization libraries.</p>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div style="background-color: var(--card-bg); padding: 20px; border-radius: var(--radius); border-left: 5px solid #ffaa00;">
                <h4 style="color: var(--primary); margin-top: 0;">Applied Statistics</h4>
                <p style="font-size: 15px; color: var(--muted); margin-bottom: 0;">Strong background in applied statistical analysis, including descriptive and inferential statistics, hypothesis testing, statistical modeling, and data interpretation for real-world problems.</p>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown(
            """
            <div style="background-color: var(--card-bg); padding: 20px; border-radius: var(--radius); border-left: 5px solid #ff4b4b;">
                <h4 style="color: var(--primary); margin-top: 0;">Machine Learning</h4>
                <p style="font-size: 15px; color: var(--muted); margin-bottom: 0;">Experience in building machine learning models for prediction and classification, including data preprocessing, feature engineering, and model evaluation.</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown("<h2>Work Experience</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h4 style="color: var(--primary); margin-bottom: 4px;">Intern — Dinas Komunikasi dan Informatika Tulungagung</h4>
        <p style="color: var(--accent); font-weight: 600; margin-top: 0; margin-bottom: 8px;">Statistical and Cryptography Intern | July 2025 - November 2025</p>
        <ul>
            <li style="color: var(--secondary);">Developed the <strong>CitraData</strong> platform for sectoral statistics visualization for Tulungagung Regency.</li>
            <li style="color: var(--secondary);">Processed and presented statistical data in the form of infographics and interactive visualizations.</li>
        </ul>
    </div>
    <div style="margin-bottom: 25px;">
        <h4 style="color: var(--primary); margin-bottom: 4px;">Intern — Badan Pusat Statistik (BPS) Tulungagung</h4>
        <p style="color: var(--accent); font-weight: 600; margin-top: 0; margin-bottom: 8px;">Statistical Assistant | November 2025 – December 2025</p>
        <ul>
            <li style="color: var(--secondary);">Managing data collection, cleaning, and verification, including data entry and data matching.</li>
            <li style="color: var(--secondary);">Conducting descriptive data analysis and visualization for internal reports, with a strong emphasis on accuracy and consistency.</li>
        </ul>
    </div>
    <div style="margin-bottom: 25px;">
        <h4 style="color: var(--primary); margin-bottom: 4px;">Personal Academic Tutor</h4>
        <p style="color: var(--accent); font-weight: 600; margin-top: 0; margin-bottom: 8px;">Mathematics and Statistics Tutor | January 2023 - Present</p>
        <ul>
            <li style="color: var(--secondary);">Enhancing students’ confidence in solving quantitative problems through a systematic and personalized approach.</li>
            <li style="color: var(--secondary);">Specializing in tutoring for mathematics and statistics subjects at high school and early university levels, resulting in an average improvement of 20–30% in exam scores.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("<h2>Education & Skills</h2>", unsafe_allow_html=True)
    
    edu_col, skill_col = st.columns(2)
    
    with edu_col:
        st.subheader("Education")
        st.markdown("""
        <div style='background: var(--card-bg); padding: 18px; border-radius: 10px; border: 1px solid #eef3f7;'>
            <h4 style='margin:0;color:var(--primary)'>Universitas Negeri Surabaya</h4>
            <p style='color: var(--secondary); margin:6px 0 0 0;'>Bachelor of Data Science (Expected Graduation 2027)</p>
        </div>
        <div style='background: var(--card-bg); padding: 18px; border-radius: 10px; border: 1px solid #eef3f7;'>
            <h4 style='margin:0;color:var(--primary)'>SMA Negeri 1 Ngunut </h4>
            <p style='color: var(--secondary); margin:6px 0 0 0;'>Mathematics and Natural Sciences (MIPA) — Top Graduate 2023</p>
        </div>
        """, unsafe_allow_html=True)

    with skill_col:
        st.subheader("Skills")
        st.markdown("""
        <div style='background: var(--card-bg); padding: 12px 16px; border-radius: 10px; border: 1px solid #eef3f7;'>
            <table style='width:100%; border-collapse: collapse;'>
                <tr style='border-bottom:1px solid #e9f0f5'>
                    <td style='padding:10px; width:35%; font-weight:700; color:var(--primary)'>Programming</td>
                    <td style='padding:10px; color:var(--secondary)'>Python (Pandas, NumPy, Scikit-learn), R, PHP</td>
                </tr>
                <tr style='border-bottom:1px solid #e9f0f5'>
                    <td style='padding:10px; font-weight:700; color:var(--primary)'>Visualization</td>
                    <td style='padding:10px; color:var(--secondary)'>Tableau, Streamlit, Matplotlib, Seaborn</td>
                </tr>
                <tr style='border-bottom:1px solid #e9f0f5'>
                    <td style='padding:10px; font-weight:700; color:var(--primary)'>Statistics</td>
                    <td style='padding:10px; color:var(--secondary)'>Regression, Hypothesis Testing, Time Series</td>
                </tr>
                <tr>
                    <td style='padding:10px; font-weight:700; color:var(--primary)'>Databases</td>
                    <td style='padding:10px; color:var(--secondary)'>SQL Basics, Excel, Google Sheets</td>
                </tr>
                <tr>
                    <td style='padding:10px; font-weight:700; color:var(--primary)'>Language</td>
                    <td style='padding:10px; color:var(--secondary)'>Javanese (Native), Indonesian (Native), English (TEP Score: 537)</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")


def render_projects():
    st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("<h2>All Projects</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:var(--secondary)'>Explore my full portfolio covering visualizations, analyses, and many more.</p>", unsafe_allow_html=True)

    # ======================
    # FILTER STATE
    # ======================
    if "project_filter" not in st.session_state:
        st.session_state.project_filter = "Show all"

    categories = [
        "Show all",
        "Data Mining",
        "Data Visualization", 
        "Scientific Paper",
        "System",
        "Design",
        "Web App",
        "Statistics"
    ]

    # ======================
    # FILTER CHIPS (HTML anchors styled) — keeps user on same page
    # ======================
    params = st.experimental_get_query_params()
    selected = params.get('filter', [st.session_state.project_filter])[0]
    chip_html = ['<div class="project-filters">']
    for cat in categories:
        active = ' active' if selected == cat else ''
        href = f'?filter={urllib.parse.quote(cat)}'
        chip_html.append(f'<a class="filter-btn{active}" href="{href}">{cat}</a>')
    chip_html.append('</div>')
    st.markdown(textwrap.dedent('\n'.join(chip_html)).lstrip(), unsafe_allow_html=True)
    st.session_state.project_filter = selected

    # ======================
    # PROJECT DATA
    # ======================

    projects = [
        {
            "title": "CitraData",
            "description": "A web-based platform for processing and visualizing sectoral statistical data, featuring interactive dashboards, data analysis, and structured public data presentation for institutional use.",
            "image": "citradata.png",
            "link": "https://diskominfo.tulungagung.go.id/citradata/",
            "categories": ["Data Visualization", "Web App" ]
        },
        
        {
            "title": "Interactive Infographics",
            "description": "A collection of interactive infographics designed to present statistical data in a clear, engaging, and easily understandable way for diverse audiences.",
            "image": "infografis.png",
            "link": "https://tulungagung.go.id/infografis/",
            "categories": ["Data Visualization" ]
        },
        {
            "title": "Mental Health Tracker",
            "description": "A application that allows users to log and monitor their mental health over time, providing insights and visualizations to help identify patterns and triggers.",
            "image": "mental.png",
            "link": "https://github.com/Sintiyarisla/Mental-Health-Tracker",
            "categories": ["Design", "Data Mining", "System" ]
        },
        {
            "title": "Paper Publication: SENADA 2025",
            "description": "A published scientific paper analyzing the impact of socio-economic and non-academic factors on academic achievement using Structural Equation Modeling (SEM).",
            "image": "senada.png",
            "link": "https://share.google/k1QGo39WB6jqrju3j",
            "categories": ["Scientific Paper", "Statistics"]
        },
        {
            "title": "Indonesian Food Recipe Recomendation Using KNN",
            "description": "A recommendation system that suggests food recipes based on ingredient similarity using the K-Nearest Neighbors (KNN) algorithm.",
            "image": "food.png",
            "link": "https://rekomendasi-menu-masakan-indonesia.streamlit.app/",
            "categories": ["Data Mining", "Web App"]
        },
        {
            "title": "Audio Separation of Two Instruments Projects",
            "description": "A project that separates audio tracks of two instruments using signal processing techniques to isolate and enhance individual sounds from a mixed audio file.",
            "image": "psd.png",
            "link": "https://github.com/Sintiyarisla/Analisis-dan-Pengolahan-Sinyal-Digital-dari-Instrumen-Musik-Pemisahan-Audio-dua-Instrumen",
            "categories": ["Data Mining", "System"]
        },
        {
            "title": "Priority-Based Goods Delivery Management System",
            "description": "A delivery management system that organizes and prioritizes shipments based on urgency and customer needs. The system ensures timely delivery by managing shipment priorities, tracking delivery status, and handling sender and destination information using efficient data structures and algorithms.",
            "image": "1.png",
            "link": "https://github.com/Sintiyarisla/Sistem-Manajemen-Pengiriman-Barang-Berdasarkan-Prioritas",
            "categories": ["System", "Data Mining", "Design"]
        },
        {
            "title": "Corruption Risk Prediction in Public Procurement Tenders Using Random Forest and SVM",
            "description": "This project applies machine learning techniques to predict corruption risk in public procurement tenders in Indonesia. By analyzing tender data, the system identifies suspicious patterns and detects potential corruption risks at an early stage. Random Forest and Support Vector Machine models are implemented and compared to support data-driven, objective, and efficient tender evaluation for oversight and policy-making purposes.",
            "image": "pmd.png",
            "link": "https://deteksi-risiko-korupsi-tender-pengadaan.streamlit.app/",
            "categories": ["Web App", "Data Mining"]
        },
        {
            "title": "Consumer Segmentation for Sales Promotion Optimization in Shopping Centers",
            "description": "This project applies K-Means and Agglomerative Clustering to segment consumers in a shopping center based on demographic and behavioral characteristics. The goal is to identify distinct customer groups and support targeted marketing and personalized promotion strategies.",
            "image": "data.png",
            "link": "https://github.com/Sintiyarisla/Segmentasi-Konsumen-untuk-Optimasi-Strategi-Promosi-Penjualan-pada-Pusat-Perbelanjaan.",
            "categories": ["Data Mining", "Statistics"]
        },
        {
            "title": "Distributed Air Quality Monitoring System",
            "description": "This project develops a distributed ETL system for air quality monitoring using Celery and RabbitMQ. The distributed architecture enables parallel processing, efficient monitoring via the Flower dashboard, and supports scalable air quality analysis.",
            "image": "etl.png",
            "link": "https://github.com/Sintiyarisla/Sistem-Monitoring-Kualitas-Udara-Berbasis-Arsitektur-Terdistribusi",
            "categories": ["System", "Data Mining"]
        },
        {
            "title": "Factor Analysis of Smart City Development in India",
            "description": "This project analyzes Smart City development in 30 cities in India using Principal Component Analysis (PCA) and Factor Analysis (FA). The results show that Smart City progress is primarily influenced by digital public services and internet accessibility. These findings highlight the importance of balancing government digital infrastructure and public connectivity to support sustainable Smart City implementation.",
            "image": "pca.png",
            "link": "https://github.com/Sintiyarisla/PCA-dan-FA-pada-30-kota-di-India",
            "categories": ["Statistics"]
        },
        {
            "title": "Sentiment Analysis of Retinol Skincare Reviews",
            "description": "This project analyzes user sentiment toward retinol serum skincare products using reviews scraped from Female Daily. Text data are processed and classified into positive, neutral, and negative sentiments using machine learning models such as Naive Bayes, KNN, and Balanced Random Forest.",
            "image": "analisis.png",
            "link": "https://github.com/Sintiyarisla/Analisis-Sentimen-Ulasan-Pengguna-Skincare-Serum-Berbahan-Retinol",
            "categories": ["Data Mining", "Data Visualization"]
        },
        {
            "title": "BFS and DFS Algorithms for Solving TSP in East Java",
            "description": "This project implements Breadth-First Search (BFS) and Depth-First Search (DFS) to solve the Traveling Salesman Problem (TSP) using inter-city distance data in East Java. The study compares both algorithms in terms of route distance, execution time, and memory usage.",
            "image": "tsp.png",
            "link": "https://github.com/Sintiyarisla/Algoritma-BFS-dan-DFS-dalam-Penyelesaian-TSP-di-Jawa-Timur",
            "categories": ["Data Mining", "System", "Web App", "Data Visualization"]
        },
        {
            "title": "Normality Testing of Student Height Distribution",
            "description": "This project analyzes the height distribution of Data Science undergraduate students (Class 2023B) using descriptive statistics and inferential methods. Normality is tested using Chi-Square, Kolmogorov–Smirnov, and Anderson–Darling tests, with results indicating that the data can be considered normally distributed at a 5% significance level.",
            "image": "normal.png",
            "link": "https://github.com/Sintiyarisla/Pengujian-Distribusi-Tinggi-Badan-Siswa-Menggunakan-Goodness-of-Fit",
            "categories": ["Statistics"]
        },
        {
            "title": "PeluangKu: Student Opportunity Discovery Mobile App Design",
            "description": "PeluangKu is a mobile application designed to help students discover verified academic and non-academic opportunities, including scholarships, competitions, internships, part-time jobs, and external organizations. The app enables opportunity search based on major, time, and category, while providing personalized recommendations, discussion space, and real-time notifications.",
            "image": "peluangku.png",
            "link": "https://www.behance.net/gallery/228735481/PeluangKu-Aplikasi-Informasi-Penunjang-Akademik",
            "categories": ["Design"]
        }
    ]

    # filter projects according to selection
    if st.session_state.project_filter == 'Show all' or not st.session_state.project_filter:
        filtered = projects
    else:
        filtered = [p for p in projects if st.session_state.project_filter in p.get('categories', [])]

    st.markdown('<div class="projects-grid">', unsafe_allow_html=True)
    cols = st.columns(3)
    def _local_image_data_uri(path: str) -> str:
        if path.startswith('http'):
            return path
        if not os.path.exists(path):
            return "https://placehold.co/800x500/e5e9ef/2E3A59?text=No+Image"
        mime, _ = mimetypes.guess_type(path)
        mime = mime or 'image/png'
        with open(path, 'rb') as f:
            data = base64.b64encode(f.read()).decode('ascii')
        return f"data:{mime};base64,{data}"

    for i, p in enumerate(filtered):
        with cols[i % 3]:
            img_src = _local_image_data_uri(p['image'])
            if p.get('link'):
                link_html = f"<a href=\"{p['link']}\" target=\"_blank\">View Project &rarr;</a>"
            else:
                link_html = '<span style="color:var(--muted);font-size:14px;">(Internal Project)</span>'

            st.markdown(f"""
                <div class="project">
                    <img src="{img_src}">
                    <h3 style="color:var(--primary);margin-top:10px">{p['title']}</h3>
                    <p style="color:var(--secondary);font-size:15px; min-height: 45px;">{p['description']}</p>
                    {link_html}
                </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

def render_contact():
    st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.markdown("<h2>Contact Me</h2>", unsafe_allow_html=True)

    st.markdown("""
    <p style="font-size: 18px; color: var(--secondary); max-width: 900px;">
        I am open to project collaborations, internship opportunities, or tutoring requests
        in Mathematics and Statistics. Please reach out via one of the methods below:
    </p>
    """, unsafe_allow_html=True)

    col_email, col_social = st.columns(2, gap="large")

    # EMAIL CARD
    with col_email:
        html_email = textwrap.dedent('''
        <div style="background-color: var(--card-bg); padding: 25px; border-radius: var(--radius); border: 1px solid #e8ecf1;">
            <h4 style="color: var(--accent); margin-top: 0;">Email</h4>
            <p style="font-size: 18px; font-weight: 600; color: var(--primary);"><a href="mailto:sintiyarisla2005@gmail.com" style="color: var(--primary); text-decoration: none;">sintiyarisla2005@gmail.com</a></p>
        </div>
        ''')
        st.markdown(html_email, unsafe_allow_html=True)

    # SOCIALS CARD
    with col_social:
        html_social = textwrap.dedent('''
        <div style="background-color: var(--card-bg); padding: 25px; border-radius: var(--radius); border: 1px solid #e8ecf1;">
            <h4 style="color: var(--accent); margin-top: 0;">Socials</h4>
            <p style="font-size: 18px; font-weight: 600; color: var(--primary); margin-bottom: 8px;">LinkedIn: <a href="https://www.linkedin.com/in/sintiya-risla/" target="_blank" style="color: var(--accent); text-decoration: none;">sintiya-risla</a></p>
            <p style="font-size: 18px; font-weight: 600; color: var(--primary); margin-bottom: 8px;">GitHub: <a href="https://github.com/Sintiyarisla" target="_blank" style="color: var(--accent); text-decoration: none;">Sintiyarisla</a></p>
            <p style="font-size: 18px; font-weight: 600; color: var(--primary); margin-bottom: 0;">Instagram: <a href="https://www.instagram.com/sintiya_risla/" target="_blank" style="color: var(--accent); text-decoration: none;">Sintiya_risla</a></p>
        </div>
        ''')
        st.markdown(html_social, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ============================
#   MAIN
# ============================

def main():
    # Single-page layout: render all sections sequentially
    render_home()
    render_about()
    render_projects()
    render_contact()


if __name__ == "__main__":

    main()
