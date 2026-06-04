import streamlit as st

def apply_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');
        
        /* الخلفية الداكنة بناءً على باليتة ألوان Ranon */
        [data-testid="stAppViewContainer"] { 
            background: linear-gradient(180deg, #1E2A38 0%, #0D1321 100%) !important; 
        }
        
        /* إخفاء القائمة الجانبية */
        [data-testid="collapsedControl"] { display: none; }
        section[data-testid="stSidebar"] { display: none; }
        
        /* ضبط الخطوط */
        * {
            font-family: 'Cairo', sans-serif !important;
        }
        h1, h2, h3, h4, p, span, label { 
            color: #F1F2F6 !important; 
        }
        
        /* توجيه النصوص لليمين */
        .stMarkdown, .stText, label, .stRadio, .stSelectbox {
            text-align: right !important;
            direction: rtl !important;
        }
        
        /* الحل الجذري للسلايدر */
        div[data-testid="stSlider"] { direction: rtl !important; }
        div[data-testid="stSlider"] > div { direction: ltr !important; }
        div[data-baseweb="slider"] { direction: ltr !important; }
        
        /* الكروت الشفافة بألوان Ranon */
        .card { 
            background: rgba(42, 59, 111, 0.5); /* #2A3B6F with opacity */
            backdrop-filter: blur(12px);
            padding: 25px; 
            border-radius: 20px; 
            border: 1px solid #6C5CE7; 
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3); 
            margin-bottom: 20px; 
            direction: rtl;
            text-align: right;
        }
        
        /* الأزرار (تدرج Ranon من البنفسجي للسماوي) */
        div.stButton > button { 
            background: linear-gradient(90deg, #6C5CE7, #00D4FF) !important; 
            color: white !important; 
            border-radius: 25px !important; 
            width: 100%; 
            transition: 0.4s; 
            font-weight: bold !important; 
            border: none !important;
        }
        div.stButton > button:hover { 
            box-shadow: 0 0 15px #00D4FF; 
            transform: scale(1.02); 
        }
    </style>
    """, unsafe_allow_html=True)