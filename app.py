import random
import streamlit as st

# Streamlit page setup
st.set_page_config(
    page_title="Bub & Bun ❤️",
    page_icon="💖",
    layout="centered"
)

# Custom pink CSS styling matching your original app
st.markdown("""
<style>
    .stApp {
        background-color: #FFC8DD;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        background-color: #FFFFFF;
    }
    .stButton>button {
        background-color: #FF5C8A;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        padding: 12px 24px;
        font-size: 18px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff3366;
        color: white;
    }
    .reason-box {
        background-color: #FFB6C1;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    h1, h2, h3, label {
        color: #4A0E17 !important;
        text-align: center;
    }
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
    st.markdown("<h1>Answer all 3 correctly to unlock &lt;3</h1>", unsafe_allow_html=True)
    st.write("")

    a1 = st.text_input("1. What is your favourite colour?", key="q1")
    a2 = st.text_input("2. What is the name of our daughter?", key="q2")
    a3 = st.text_input("3. What is our usual date cafe?", key="q3")

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
    st.markdown("<h1>Why Bub Loves Bun &lt;3</h1>", unsafe_allow_html=True)
    
    st.markdown(
        f"<div class='reason-box'><h3>{st.session_state.current_reason}</h3></div>",
        unsafe_allow_html=True
    )

    if st.button("❤️ Click for a Reason ❤️️"):
        st.session_state.current_reason = random.choice(reasons)
        st.rerun()