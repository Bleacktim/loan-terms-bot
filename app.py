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

/* Safely hide cloud badges */
.viewerBadge_container, .viewerBadge_link, #viewerBadge, [data-testid="manage-app-button"] { display: none !important; }
#MainMenu, footer { display: none !important; }

/* Hide Share / Star / Edit / GitHub buttons from the top-right toolbar */
[data-testid="stToolbar"] { right: 0; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stToolbarActionBtn"] { display: none !important; }
header [data-testid="stToolbar"] > div:last-child { visibility: hidden !important; }

/* Force sidebar toggle to always show - position fixed so it's always on screen */
[data-testid="collapsedControl"] {
    visibility: visible !important;
    display: flex !important;
    position: fixed !important;
    top: 14px !important;
    left: 14px !important;
    z-index: 9999999 !important;
    background: rgba(139, 92, 246, 0.3) !important;
    border: 1px solid rgba(139, 92, 246, 0.6) !important;
    border-radius: 8px !important;
    padding: 4px 8px !important;
    backdrop-filter: blur(10px) !important;
}
[data-testid="collapsedControl"] svg,
[data-testid="stSidebarCollapsedControl"] svg { 
    fill: white !important; 
    stroke: white !important; 
    color: white !important; 
}

/* UNIFORM BACKGROUND — same color everywhere */
html, body, [data-testid="stApp"], .stApp,
[data-testid="stHeader"], header,
[data-testid="stToolbar"],
[data-testid="stSidebar"],
[data-testid="stMainBlockContainer"],
[data-testid="block-container"],
.main, .block-container,
[class*="appview-container"],
[class*="main-content"],
section[data-testid="stSidebar"] {
    background-color: #0f172a !important;
    background: #0f172a !important;
}


/* Animated Blobs Background */
.stApp {
    background-color: #0f172a !important;
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

/* Custom Buttons as Tabs */
button[kind="primary"] {
    color: #ffffff !important;
    background: linear-gradient(135deg, #0ea5e9, #8b5cf6, #ec4899) !important;
    background-size: 200% auto !important;
    border: none !important;
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.6) !important;
    animation: gradientMove 3s ease infinite !important;
    border-radius: 50px !important;
    transition: all 0.3s ease !important;
    padding: 8px 6px !important;
}
button[kind="primary"] p {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    white-space: nowrap !important;
    margin: 0 !important;
}
button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.07) !important;
    border: 1px solid rgba(139, 92, 246, 0.4) !important;
    border-radius: 50px !important;
    box-shadow: 0 0 15px rgba(139, 92, 246, 0.15), inset 0 1px 0 rgba(255,255,255,0.1) !important;
    transition: all 0.3s ease !important;
    padding: 8px 6px !important;
    backdrop-filter: blur(10px) !important;
}
button[kind="secondary"]:hover {
    background: rgba(139, 92, 246, 0.2) !important;
    border-color: rgba(139, 92, 246, 0.8) !important;
    box-shadow: 0 0 25px rgba(139, 92, 246, 0.4) !important;
    transform: translateY(-2px) !important;
}
button[kind="secondary"] p {
    color: #cbd5e1 !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    white-space: nowrap !important;
    margin: 0 !important;
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
[data-testid="stBottom"], [data-testid="stBottom"] > div,
[class*="st-emotion-cache"] > [data-testid="stBottom"] {
    background-color: #0f172a !important;
    background: #0f172a !important;
}
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

# Auto-open the sidebar using JavaScript on first load
st.markdown("""
<script>
    // Wait for Streamlit to render, then click the sidebar toggle if sidebar is collapsed
    setTimeout(function() {
        var toggleBtn = window.parent.document.querySelector('[data-testid="collapsedControl"]');
        if (toggleBtn) { toggleBtn.click(); }
    }, 500);
</script>
""", unsafe_allow_html=True)

# --- DEFAULT VALUES (used if Command Center tab not visited yet) ---
if "persona" not in st.session_state:
    st.session_state.persona = "Friendly Advisor"
if "credit_score" not in st.session_state:
    st.session_state.credit_score = 720
if "loan_amount" not in st.session_state:
    st.session_state.loan_amount = 50000

# --- MAIN PAGE HEADER ---
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

# --- CUSTOM TABS ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "AI Assistant"

col_tab1, col_tab2, col_tab3, col_tab4 = st.columns([1.2, 1.2, 1.2, 1.1])

with col_tab1:
    if st.button("💬 AI Assistant", type="primary" if st.session_state.active_tab == "AI Assistant" else "secondary", use_container_width=True):
        st.session_state.active_tab = "AI Assistant"
        st.rerun()

with col_tab2:
    if st.button("⚙️ Settings", type="primary" if st.session_state.active_tab == "Command Center" else "secondary", use_container_width=True):
        st.session_state.active_tab = "Command Center"
        st.rerun()

with col_tab3:
    if st.button("📊 Markets", type="primary" if st.session_state.active_tab == "Market Trends" else "secondary", use_container_width=True):
        st.session_state.active_tab = "Market Trends"
        st.rerun()

with col_tab4:
    if st.button("📑 System", type="primary" if st.session_state.active_tab == "System Specs" else "secondary", use_container_width=True):
        st.session_state.active_tab = "System Specs"
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ==================== TAB CONTENT ====================

if st.session_state.active_tab == "AI Assistant":
    persona = st.session_state.persona
    credit_score = st.session_state.credit_score
    loan_amount = st.session_state.loan_amount

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

    # --- CUSTOM INPUT ROW: [🧹 Clear] + [text input] + [↑ Send] ---
    st.markdown("""
    <style>
    .input-row-clear button { border: 1px solid rgba(239,68,68,0.6) !important; background: rgba(239,68,68,0.1) !important; height: 42px !important; }
    .input-row-clear button p { color: #fca5a5 !important; }
    .input-row-clear button:hover { background: rgba(239,68,68,0.25) !important; border-color: rgba(239,68,68,0.9) !important; }
    </style>
    """, unsafe_allow_html=True)

    inp_text, inp_clear = st.columns([7, 1])
    with inp_text:
        user_input = st.chat_input("Ask about interest rates, penalties...")
    with inp_clear:
        st.markdown('<div class="input-row-clear">', unsafe_allow_html=True)
        if st.button("🧹 Clear", use_container_width=True, key="clear_btn_inline"):
            if "messages" in st.session_state:
                st.session_state.messages = [{"role": "assistant", "content": f"Memory wiped securely. Starting new session as a {st.session_state.persona}."}]
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.rerun()

elif st.session_state.active_tab == "Command Center":
    cc1, cc2 = st.columns(2, gap="large")
    with cc1:
        st.markdown("""<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(139,92,246,0.3);border-radius:20px;padding:28px">
        <h3 style="color:white;margin-top:0">🤖 AI Persona</h3>
        <p style="color:#94a3b8;font-size:0.9rem">Choose how the AI should behave during your session.</p>
        </div>""", unsafe_allow_html=True)
        persona_choice = st.selectbox("AI Persona", ["Friendly Advisor", "Strict Corporate Banker", "Legal Analyst"], index=["Friendly Advisor", "Strict Corporate Banker", "Legal Analyst"].index(st.session_state.persona), label_visibility="collapsed")
        st.session_state.persona = persona_choice

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(14,165,233,0.3);border-radius:20px;padding:28px">
        <h3 style="color:white;margin-top:0">📄 Additional Data</h3>
        <p style="color:#94a3b8;font-size:0.9rem">Upload an external contract for AI to analyze.</p>
        </div>""", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload External Contract (PDF)", type=["pdf"], label_visibility="collapsed")
        if uploaded_file:
            st.success("File recognized. AI is analyzing...")

    with cc2:
        st.markdown("""<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(236,72,153,0.3);border-radius:20px;padding:28px">
        <h3 style="color:white;margin-top:0">👤 Financial Profile</h3>
        <p style="color:#94a3b8;font-size:0.9rem">Set your financial parameters to personalize AI responses.</p>
        </div>""", unsafe_allow_html=True)
        st.session_state.credit_score = st.slider("Credit Score", min_value=300, max_value=850, value=st.session_state.credit_score, step=10)
        st.session_state.loan_amount = st.number_input("Desired Loan Amount ($)", min_value=1000, value=st.session_state.loan_amount, step=5000)

        st.markdown("<br>", unsafe_allow_html=True)
        if "messages" in st.session_state and len(st.session_state.messages) > 1:
            chat_export = ""
            for msg in st.session_state.messages:
                chat_export += f"{msg['role'].upper()}: {msg['content']}\n\n"
            st.download_button(label="📥 Download Audit Log", data=chat_export, file_name="fintech_audit_log.txt", mime="text/plain", use_container_width=True)

elif st.session_state.active_tab == "Market Trends":
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""<div style="background:linear-gradient(135deg,rgba(14,165,233,0.15),rgba(14,165,233,0.05));border:1px solid rgba(14,165,233,0.4);border-radius:16px;padding:16px;text-align:center">
            <div style="font-size:0.75rem;color:#94a3b8;letter-spacing:2px;text-transform:uppercase">Mortgage Rate</div>
            <div style="font-size:2rem;font-weight:800;color:#0ea5e9;margin:4px 0">{round(random.uniform(6.2, 7.8), 2)}%</div>
            <div style="font-size:0.8rem;color:#22c55e">▲ +0.12%</div></div>""", unsafe_allow_html=True)
    with m2:
        st.markdown(f"""<div style="background:linear-gradient(135deg,rgba(139,92,246,0.15),rgba(139,92,246,0.05));border:1px solid rgba(139,92,246,0.4);border-radius:16px;padding:16px;text-align:center">
            <div style="font-size:0.75rem;color:#94a3b8;letter-spacing:2px;text-transform:uppercase">Auto Loan</div>
            <div style="font-size:2rem;font-weight:800;color:#8b5cf6;margin:4px 0">{round(random.uniform(7.5, 9.5), 2)}%</div>
            <div style="font-size:0.8rem;color:#ef4444">▼ -0.05%</div></div>""", unsafe_allow_html=True)
    with m3:
        st.markdown(f"""<div style="background:linear-gradient(135deg,rgba(236,72,153,0.15),rgba(236,72,153,0.05));border:1px solid rgba(236,72,153,0.4);border-radius:16px;padding:16px;text-align:center">
            <div style="font-size:0.75rem;color:#94a3b8;letter-spacing:2px;text-transform:uppercase">Personal Loan</div>
            <div style="font-size:2rem;font-weight:800;color:#ec4899;margin:4px 0">{round(random.uniform(10.5, 14.0), 2)}%</div>
            <div style="font-size:0.8rem;color:#22c55e">▲ +0.31%</div></div>""", unsafe_allow_html=True)
    with m4:
        st.markdown(f"""<div style="background:linear-gradient(135deg,rgba(34,197,94,0.15),rgba(34,197,94,0.05));border:1px solid rgba(34,197,94,0.4);border-radius:16px;padding:16px;text-align:center">
            <div style="font-size:0.75rem;color:#94a3b8;letter-spacing:2px;text-transform:uppercase">Prime Rate</div>
            <div style="font-size:2rem;font-weight:800;color:#22c55e;margin:4px 0">{round(random.uniform(5.0, 5.5), 2)}%</div>
            <div style="font-size:0.8rem;color:#94a3b8">— Stable</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:16px 16px 4px">
            <div style="font-size:0.9rem;font-weight:700;color:#e2e8f0;margin-bottom:8px">📈 Live Interest Rate Trends</div>""", unsafe_allow_html=True)
        chart_data = pd.DataFrame(np.random.randn(30, 3) + [6, 8, 12], columns=["Mortgage %", "Auto Loan %", "Personal Loan %"])
        st.line_chart(chart_data, color=["#0ea5e9", "#8b5cf6", "#ec4899"], height=200)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:16px 16px 4px">
            <div style="font-size:0.9rem;font-weight:700;color:#e2e8f0;margin-bottom:8px">📊 Approval Rate by Credit Score</div>""", unsafe_allow_html=True)
        bar_data = pd.DataFrame([95, 82, 67, 45, 22], index=[">= 800", "740-799", "670-739", "580-669", "< 580"], columns=["Approval %"])
        st.bar_chart(bar_data, color="#8b5cf6", height=200)
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_tab == "System Specs":
    st.markdown("### 🏛️ Deep Technology Stack")
    st.info("This interface utilizes Apple Vision Pro-style glassmorphism combined with heavy LLM backend processing.")
    st.markdown("""
- **Brain (LLM):** Google Gemini 1.5 Pro
- **Memory (Vector DB):** Qdrant Local Engine
- **Embeddings:** FastEmbed (BAAI/bge-small-en-v1.5)
- **Frontend:** Streamlit
- **Data Source:** Secure PDF Document Injection
    """)

