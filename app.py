import streamlit as st
from agent import ask

st.set_page_config(page_title="FinTech AI Engine", page_icon="🏦", layout="centered")

custom_css = """
<style>
/* Ultra-Premium FinTech Holographic Theme */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

/* Hide default Streamlit UI for app-like feel */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Dynamic Ambient Background */
.stApp {
    background: radial-gradient(circle at 15% 50%, rgba(15, 23, 42, 1), rgba(15, 23, 42, 0.8)), 
                radial-gradient(circle at 85% 30%, rgba(49, 46, 129, 0.9), rgba(0, 0, 0, 1)) !important;
    background-size: 200% 200% !important;
    animation: gradientShift 15s ease infinite !important;
    font-family: 'Outfit', sans-serif !important;
    color: #e2e8f0 !important;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating Header Glow */
.premium-header {
    text-align: center;
    padding: 30px 0;
    animation: float 6s ease-in-out infinite, pulseGlow 3s alternate infinite;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}
@keyframes pulseGlow {
    from { text-shadow: 0 0 10px rgba(0,242,254,0.1); }
    to { text-shadow: 0 0 30px rgba(0,242,254,0.4); }
}

.premium-header h1 {
    font-size: 3.8rem;
    font-weight: 700;
    background: linear-gradient(90deg, #00f2fe, #4facfe, #00f2fe);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s linear infinite;
    margin: 0;
}
@keyframes shine {
    to { background-position: 200% center; }
}
.premium-header p {
    color: #94a3b8;
    font-size: 1.1rem;
    font-weight: 400;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-top: 10px;
}

/* Glassmorphism Chat Messages Box */
.stChatMessage {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 20px !important;
    padding: 20px !important;
    backdrop-filter: blur(16px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
    margin-bottom: 15px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease !important;
}
.stChatMessage:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 40px 0 rgba(0, 242, 254, 0.15) !important;
    border: 1px solid rgba(0, 242, 254, 0.3) !important;
}

/* Neon Chat Input Styling */
.stChatInputContainer {
    background: rgba(0, 0, 0, 0.6) !important;
    border: 1px solid rgba(0, 242, 254, 0.3) !important;
    border-radius: 30px !important;
    backdrop-filter: blur(20px) !important;
    box-shadow: 0 0 20px rgba(0, 242, 254, 0.1) !important;
    transition: all 0.3s ease !important;
    padding: 5px !important;
}
.stChatInputContainer:focus-within {
    border: 1px solid rgba(0, 242, 254, 0.9) !important;
    box-shadow: 0 0 40px rgba(0, 242, 254, 0.4) !important;
}

/* Gradient Avatars */
[data-testid="stChatMessageAvatarUser"] {
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%) !important;
}
[data-testid="stChatMessageAvatarAssistant"] {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.markdown("""
<div class="premium-header">
    <h1>🏦 FinTech AI Engine</h1>
    <p>Enterprise-grade Loan Term Analysis</p>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about interest rates, penalties..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = ask(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
