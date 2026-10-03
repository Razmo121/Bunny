import random
import os
import base64
import streamlit as st

# Streamlit Page Setup
st.set_page_config(
    page_title="Bub & Bun ❤️",
    page_icon="💖",
    layout="centered"
)

# Helper function to encode image to Base64 for button background
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Global Styles
st.markdown("""
<style>
    /* Constrain width to simulate desktop/mobile window */
    .block-container {
        max-width: 450px !important;
        padding-top: 3rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Times New Roman bold headers matching Tkinter */
    .tkinter-title {
        font-family: 'Times New Roman', Times, serif;
        font-size: 28px;
        font-weight: bold;
        color: #000000;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Question labels */
    .tkinter-label {
        font-family: Helvetica, Arial, sans-serif;
        font-size: 16px;
        color: #000000;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 4px;
    }

    /* Centered Text Inputs */
    .stTextInput > div > div > input {
        font-family: Helvetica, Arial, sans-serif;
        font-size: 16px;
        text-align: center;
        background-color: #FFFFFF;
        color: #000000;
        border: 1px solid #767676;
        border-radius: 4px;
    }

    /* Hide default Streamlit header/footer for clean app view */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# List of reasons
reasons = [
    "You make me smile", "I feel happy when I talk to you", "You are the cutest person ever",
    "You always support me", "I love your laugh", "Because you're YOU", "You are my favourite human",
    "I love how you care about me", "Your smile brightens my worst days", "You make me feel loved",
    "You listen to all my nonsense patiently", "You support my dreams", "You are the first person I want to share news with",
    "You care deeply about others", "You always try to improve yourself", "You laugh at my dumb jokes",
    "You never give up on me", "You motivate me to be better", "You look cute when you’re angry",
    "Your eyes feel like home", "You make ordinary moments feel special", "You understand me without words",
    "You trust me", "You are loyal", "You are smart and talented", "You're funny without trying",
    "Your hugs feel magical", "Your voice calms me down", "You bring peace into my chaos",
    "You care about my feelings", "You notice every small detail about me", "Your random texts make me smile",
    "You’re beautiful inside and out", "You love me the way I am", "You believe in us",
    "Your hair is always perfect", "You are strong in tough times", "You’re my favourite distraction",
    "I can be myself around you", "You make me feel wanted", "You are unique",
    "You look adorable without trying", "You forgive quickly", "You show affection in the cutest ways",
    "You make the best memes", "You make me laugh instantly", "You're patient with me",
    "You inspire me", "You are my safe place", "You care about my health",
    "You love food as much as I do", "You cheer for me always", "You smell amazing",
    "You tolerate my weird habits", "You celebrate even my small achievements", "You make me feel lucky",
    "You get excited about small things", "You blush in the cutest way", "Every outfit looks perfect on you",
    "You give me the cutest nicknames", "You appreciate my efforts", "You’re honest",
    "You share your secrets with me", "You understand my silence", "You make me feel special every single day",
    "You hold my hand randomly", "You somehow handle all my chaos", "You are my comfort person",
    "You believe in love", "You take care of me when I'm sick", "You make me laugh till I can’t breathe",
    "You are thoughtful", "You love animals", "You listen even when I ramble",
    "You always try to make things right", "You push me to do better", "You look adorable when you’re sleepy",
    "Your jealousy is cute", "You make me feel proud", "You know how to calm me",
    "You have a big heart", "You make my life happier", "You are my best friend",
    "You make everything better just by being there", "You’re adventurous", "You respect others",
    "You genuinely understand me", "Your laugh is the cutest thing ever", "You give amazing compliments",
    "You make me feel handsome", "You never demand perfection", "You love surprising me",
    "You work hard", "You share food with me — and that’s true love", "You make me excited about the future",
    "You accept my flaws", "You love the weirdest parts of me", "You bring out the best in me",
    "You are adorably dramatic", "You’re playful and fun", "You’re my dream partner",
    "You make my heart feel full", "You’re unpredictably cute", "You still laugh at my lamest jokes",
    "You’re the first and last person I think of every day", "You look extra cute when you’re focused",
    "You make love feel easy", "You are my everything"
]

answers = ["mlue", "pengu", "beanshot cafe"]

# Session State Initializations
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False
if "current_reason" not in st.session_state:
    st.session_state.current_reason = "Click the heart! <3"

# =====================================================
#                 QUESTION PAGE
# =====================================================
if not st.session_state.unlocked:
    st.markdown("""
    <style>
        .stApp {
            background-color: #FFC8DD;
        }
        div[data-testid="stButton"] > button {
            background-color: #FF5C8A !important;
            color: white !important;
            font-family: Helvetica, Arial, sans-serif !important;
            font-size: 18px !important;
            font-weight: bold !important;
            border: 2px solid #D83366 !important;
            border-radius: 4px !important;
            padding: 6px 24px !important;
            display: block !important;
            margin: 0 auto !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='tkinter-title'>Answer all 3 correctly to unlock &lt;3</div>", unsafe_allow_html=True)

    st.markdown("<div class='tkinter-label'>1. What is the your favourite colour?</div>", unsafe_allow_html=True)
    a1 = st.text_input("", key="q1", label_visibility="collapsed")

    st.markdown("<div class='tkinter-label'>2. What is the name of our daughter?</div>", unsafe_allow_html=True)
    a2 = st.text_input("", key="q2", label_visibility="collapsed")

    st.markdown("<div class='tkinter-label'>3. What is our usual date cafe?</div>", unsafe_allow_html=True)
    a3 = st.text_input("", key="q3", label_visibility="collapsed")

    st.write("")
    if st.button("Submit 💘"):
        user_ans = [a1.strip().lower(), a2.strip().lower(), a3.strip().lower()]
        if user_ans == answers:
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("Oops! Wrong answer 😜 Try again!")

# =====================================================
#                   LOVE PAGE
# =====================================================
else:
    heart_b64 = get_base64_image("heart.png")

    st.markdown(f"""
    <style>
        .stApp {{
            background-color: #FFB6C1;
        }}
        .reason-text {{
            font-family: Helvetica, Arial, sans-serif;
            font-size: 18px;
            color: #000000;
            text-align: center;
            margin-top: 35px;
            margin-bottom: 35px;
            min-height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        div[data-testid="stButton"] > button {{
            background-image: url('data:image/png;base64,{heart_b64}') !important;
            background-color: transparent !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            border: none !important;
            outline: none !important;
            width: 120px !important;
            height: 120px !important;
            box-shadow: none !important;
            cursor: pointer !important;
            color: transparent !important;
            margin: 0 auto !important;
            display: block !important;
        }}
        div[data-testid="stButton"] > button:hover,
        div[data-testid="stButton"] > button:focus,
        div[data-testid="stButton"] > button:active {{
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            transform: scale(1.08);
            transition: transform 0.15s ease-in-out;
        }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='tkinter-title'>Why Bub Loves Bun &lt;3</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='reason-text'>{st.session_state.current_reason}</div>", unsafe_allow_html=True)

    # Clickable Heart Button
    if st.button(" ", key="heart_btn"):
        st.session_state.current_reason = random.choice(reasons)
        st.rerun()
