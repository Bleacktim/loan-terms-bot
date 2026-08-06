import streamlit as st
from agent import ask

st.set_page_config(page_title="FinTech AI Engine", page_icon="🏦", layout="centered")

custom_css = """
<style>
/* Ultimate Premium FinTech Holographic Theme */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&display=swap');

.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e1b4b, #000000, #312e81) !important;
    background-size: 400% 400% !important;
    animation: gradientBG 15s ease infinite !important;
    font-family: 'Space Grotesk', sans-serif !important;
    color: white !important;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating Header Glow */
.premium-header {
    text-align: center;
    padding: 20px 0;
    animation: float 6s ease-in-out infinite;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

.premium-header h1 {
    font-size: 3rem;
    font-weight: 700;
    letter-spacing: -1px;
    background: linear-gradient(to right, #00f2fe, #4facfe, #00f2fe);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s linear infinite;
    margin-bottom: 5px;
}
@keyframes shine {
    to { background-position: 200% center; }
}
.premium-header p {
    color: #cbd5e1;
    font-size: 1.2rem;
    font-weight: 300;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Chat Messages */
.stChatMessage {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 15px !important;
    padding: 15px !important;
    backdrop-filter: blur(10px) !important;
    margin-bottom: 10px !important;
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
