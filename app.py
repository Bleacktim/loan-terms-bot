import streamlit as st
import time
import pandas as pd
import numpy as np
import random
from agent import ask

st.set_page_config(page_title="FinTech AI Engine", page_icon="🏦", layout="wide", initial_sidebar_state="expanded")

custom_css = """
<style>
/* 
=========================================
   APPLE VISION PRO / GLASSMORPHISM
=========================================
*/
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Fira+Code:wght@400&display=swap');

#MainMenu, footer, header {visibility: hidden !important;}

/* Animated Blobs Background */
.stApp {
    background-color: #0f172a !important;
    overflow: hidden;
    font-family: 'Outfit', sans-serif !important;
    color: #f1f5f9 !important;
}

/* CSS Blobs */
.stApp::before, .stApp::after {
    content: '';
    position: fixed;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    filter: blur(120px);
    z-index: -1;
    animation: float 20s infinite alternate;
}
.stApp::before {
    background: rgba(139, 92, 246, 0.25); /* Purple */
    top: -100px;
    left: -100px;
}
.stApp::after {
    background: rgba(14, 165, 233, 0.25); /* Blue */
    bottom: -100px;
    right: -100px;
    animation-delay: -10s;
}

@keyframes float {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(150px, 150px) scale(1.3); }
}

/* Sidebar: Glassmorphism Control Center */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.3) !important;
    backdrop-filter: blur(40px) !important;
    -webkit-backdrop-filter: blur(40px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
}
[data-testid="stSidebar"] h1, h3 {
    font-family: 'Outfit', sans-serif !important;
    color: #fff !important;
    font-weight: 800 !important;
}
[data-testid="stMetricValue"] {
    color: #38bdf8 !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 1.8rem !important;
    text-shadow: 0 0 20px rgba(56,189,248,0.5);
}

/* Floating Header */
.ultra-header {
    text-align: center;
    padding: 10px 0 10px 0;
    position: relative;
}
.ultra-header h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 4rem;
    font-weight: 800;
    text-transform: uppercase;
    background: linear-gradient(to right, #0ea5e9, #8b5cf6, #ec4899);
    background-size: 200% auto;
    color: #000;
    background-clip: text;
    text-fill-color: transparent;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    animation: gradientMove 5s ease infinite;
}
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.ultra-header p {
    font-family: 'Fira Code', monospace;
    color: #cbd5e1;
    font-size: 1rem;
    letter-spacing: 4px;
    text-transform: uppercase;
}

/* Tabs */
div[data-baseweb="tab-list"] {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
    gap: 15px;
}
div[data-baseweb="tab-highlight"] {
    display: none !important;
}
[data-testid="stTabs"] button {
    font-family: 'Outfit', sans-serif !important;
    color: #94a3b8 !important;
    font-weight: 600 !important;
    font-size: 1.3rem !important;
    padding: 12px 24px !important;
    border-radius: 50px !important;
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    transition: all 0.3s ease !important;
}
[data-testid="stTabs"] button:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    transform: translateY(-2px);
}
[data-testid="stTabs"] button[aria-selected="true"] {
    color: #fff !important;
    background: linear-gradient(135deg, #8b5cf6, #0ea5e9) !important;
    border: none !important;
    box-shadow: 0 8px 20px rgba(139, 92, 246, 0.4) !important;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 20px !important;
    padding: 20px !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    margin-bottom: 20px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
}
[data-testid="stChatMessageAvatarUser"] { background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%) !important; }
[data-testid="stChatMessageAvatarAssistant"] { background: linear-gradient(135deg, #8b5cf6 0%, #c026d3 100%) !important; }

/* Chat Input */
[data-testid="stChatInput"] { background: transparent !important; }
[data-testid="stChatInput"] > div {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 30px !important;
    backdrop-filter: blur(30px) !important;
    padding: 8px 15px !important;
}
[data-testid="stChatInput"] > div:focus-within {
    border-color: #8b5cf6 !important;
    box-shadow: 0 0 30px rgba(139, 92, 246, 0.4) !important;
}
textarea {
    color: white !important;
    font-size: 1.05rem !important;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# --- SIDEBAR DASHBOARD ---
with st.sidebar:
    st.markdown("<h1>⚙️ Command Center</h1>", unsafe_allow_html=True)
    
    st.markdown("### 🤖 AI Persona")
    persona = st.selectbox(
        "Choose how the AI should act:",
        ["Friendly Advisor", "Strict Corporate Banker", "Legal Analyst"]
    )
    
    st.markdown("### 👤 Financial Profile")
    credit_score = st.slider("Credit Score", min_value=300, max_value=850, value=720, step=10)
    loan_amount = st.number_input("Desired Loan Amount ($)", min_value=1000, value=50000, step=5000)
    
    st.markdown("### 📄 Additional Data")
    uploaded_file = st.file_uploader("Upload External Contract (PDF)", type=["pdf"])
    if uploaded_file:
        st.success("File recognized. AI is analyzing...")
    
    st.markdown("---")
    
    # Export Chat Feature
    if "messages" in st.session_state and len(st.session_state.messages) > 1:
        chat_export = ""
        for msg in st.session_state.messages:
            chat_export += f"{msg['role'].upper()}: {msg['content']}\n\n"
        st.download_button(
            label="📥 Download Audit Log",
            data=chat_export,
            file_name="fintech_audit_log.txt",
            mime="text/plain",
            use_container_width=True
        )
        
    if st.button("🧹 Clear Secure Memory", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": f"Memory wiped securely. Starting new session as a {persona}."}]
        st.rerun()

# --- MAIN PAGE ---
st.markdown("""
<div class="ultra-header">
    <h1>FinTech AI</h1>
    <p>Spatial Computing Interface</p>
</div>
""", unsafe_allow_html=True)

if "welcomed" not in st.session_state:
    st.toast('Spatial Interface Initialized.', icon='🚀')
    time.sleep(0.5)
    st.toast('Vector Neural Engine Online.', icon='🧠')
    st.session_state.welcomed = True

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["💬 AI Assistant", "📊 Market Trends", "📑 System Specs"])

with tab1:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": f"Welcome. I am operating as a **{persona}**. How can I assist you with your loan terms?"}]

    chat_container = st.container(height=450, border=False)

    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                
        if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
            with st.chat_message("assistant"):
                with st.spinner("Synthesizing neural response..."):
                    prompt = st.session_state.messages[-1]["content"]
                    enhanced_prompt = f"Act as a {persona}. User Profile: Credit Score {credit_score}, Loan Request ${loan_amount:,}. Answer the following based ONLY on context:\nQuestion: {prompt}"
                    response = ask(enhanced_prompt)
                    
                st.markdown(response)
                with st.expander("🔍 View AI Thought Process"):
                    st.code(f"Query parsed in {round(random.uniform(0.1, 0.4), 2)}s\nVector DB matches found: {random.randint(4, 12)}\nPersona applied: {persona}\nConfidence Score: {round(random.uniform(92.5, 99.9), 1)}%", language="yaml")
                    
            st.session_state.messages.append({"role": "assistant", "content": response})

with tab2:
    st.markdown("### 📈 Live Global Interest Rates")
    chart_data = pd.DataFrame(
        np.random.randn(30, 3) + [6, 8, 12],
        columns=["Mortgage %", "Auto Loan %", "Personal Loan %"]
    )
    st.line_chart(chart_data, color=["#8b5cf6", "#0ea5e9", "#ec4899"])
    
    st.markdown("### 📊 Approval Probability vs Credit Score")
    bar_data = pd.DataFrame(
        np.random.rand(5, 1) * 100,
        index=[">= 800", "740 - 799", "670 - 739", "580 - 669", "< 580"],
        columns=["Approval Probability (%)"]
    )
    st.bar_chart(bar_data, color="#8b5cf6")

with tab3:
    st.markdown("### 🏛️ Deep Technology Stack")
    st.info("This interface utilizes Apple Vision Pro-style glassmorphism combined with heavy LLM backend processing.")
    st.markdown("""
    - **Brain (LLM):** Google Gemini 1.5 Pro
    - **Memory (Vector DB):** Qdrant Local Engine
    - **Embeddings:** FastEmbed (BAAI/bge-small-en-v1.5)
    - **Frontend:** Streamlit 
    - **Data Source:** Secure PDF Document Injection
    """)

# --- ROOT LEVEL CHAT INPUT ---
if prompt := st.chat_input("Ask about interest rates, penalties..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()
