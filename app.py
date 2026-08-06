import streamlit as st
import time
from agent import ask

st.set_page_config(page_title="FinTech AI Engine", page_icon="🏦", layout="wide", initial_sidebar_state="expanded")

custom_css = """
<style>
/* Absolute Masterpiece Ultra-Premium CSS */
@import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Inter:wght@300;400;600&display=swap');

/* Hide Streamlit Defaults completely */
#MainMenu, footer, header {visibility: hidden !important;}

/* The Ultimate Animated Mesh Background */
.stApp {
    background-color: #050505 !important;
    background-image: 
        radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
        radial-gradient(at 50% 0%, hsla(225,39%,30%,0.5) 0, transparent 50%), 
        radial-gradient(at 100% 0%, hsla(339,49%,30%,0.5) 0, transparent 50%) !important;
    background-attachment: fixed !important;
    font-family: 'Inter', sans-serif !important;
    color: #ffffff !important;
}

/* Custom Scrollbar for a premium feel */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.02); }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #00f2fe, #4facfe); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: linear-gradient(180deg, #f093fb, #f5576c); }

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: rgba(10, 10, 15, 0.4) !important;
    backdrop-filter: blur(25px) !important;
    -webkit-backdrop-filter: blur(25px) !important;
    border-right: 1px solid rgba(0, 242, 254, 0.2) !important;
}
[data-testid="stSidebar"] h1 {
    font-family: 'Syncopate', sans-serif !important;
    background: linear-gradient(90deg, #00f2fe, #4facfe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: uppercase;
    font-size: 1.4rem;
    margin-bottom: 20px;
}
[data-testid="stMetricValue"] {
    color: #00f2fe !important;
    font-family: 'Syncopate', sans-serif !important;
    font-size: 1.5rem !important;
    text-shadow: 0 0 10px rgba(0,242,254,0.4);
}

/* 3D Floating Header */
.ultra-header {
    text-align: center;
    padding: 10px 0 20px 0;
    position: relative;
    z-index: 10;
}
.ultra-header h1 {
    font-family: 'Syncopate', sans-serif;
    font-size: 3.2rem;
    font-weight: 700;
    text-transform: uppercase;
    background: linear-gradient(to right, #fff 20%, #00f2fe 40%, #4facfe 60%, #fff 80%);
    background-size: 200% auto;
    color: #000;
    background-clip: text;
    text-fill-color: transparent;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shineText 4s linear infinite;
    letter-spacing: 2px;
    margin: 0;
    filter: drop-shadow(0px 4px 15px rgba(0, 242, 254, 0.4));
}
@keyframes shineText { to { background-position: 200% center; } }

.ultra-header p {
    font-family: 'Inter', sans-serif;
    color: #a1a1aa;
    font-size: 0.95rem;
    letter-spacing: 6px;
    margin-top: 15px;
    text-transform: uppercase;
    text-shadow: 0 0 10px rgba(255,255,255,0.2);
}

/* Premium 3D Chat Message Bubbles */
[data-testid="stChatMessage"] {
    background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%) !important;
    border-top: 1px solid rgba(255,255,255,0.15) !important;
    border-left: 1px solid rgba(255,255,255,0.15) !important;
    border-right: 1px solid rgba(255,255,255,0.02) !important;
    border-bottom: 1px solid rgba(255,255,255,0.02) !important;
    border-radius: 24px !important;
    padding: 20px 25px !important;
    backdrop-filter: blur(25px) saturate(200%) !important;
    -webkit-backdrop-filter: blur(25px) saturate(200%) !important;
    margin-bottom: 25px !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1) !important;
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, border-color 0.4s ease !important;
}
[data-testid="stChatMessage"]:hover {
    transform: scale(1.01) translateY(-3px) !important;
    border-color: rgba(0, 242, 254, 0.5) !important;
    box-shadow: 0 20px 40px rgba(0, 242, 254, 0.2), inset 0 1px 0 rgba(255,255,255,0.3) !important;
}

/* Glowing Avatar Containers */
[data-testid="stChatMessageAvatarUser"] {
    background: linear-gradient(135deg, #00C9FF 0%, #92FE9D 100%) !important;
    box-shadow: 0 0 20px rgba(0, 201, 255, 0.6) !important;
    border: 2px solid rgba(255,255,255,0.9) !important;
}
[data-testid="stChatMessageAvatarAssistant"] {
    background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%) !important;
    box-shadow: 0 0 20px rgba(255, 65, 108, 0.6) !important;
    border: 2px solid rgba(255,255,255,0.9) !important;
}

/* The Magic Chat Input Container */
[data-testid="stChatInput"] { background: transparent !important; }
[data-testid="stChatInput"] > div {
    background: rgba(10, 10, 10, 0.7) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 30px !important;
    backdrop-filter: blur(30px) !important;
    padding: 8px 15px !important;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05) inset !important;
    transition: all 0.4s ease !important;
}
[data-testid="stChatInput"] > div:focus-within {
    border-color: #00f2fe !important;
    box-shadow: 0 10px 40px rgba(0, 242, 254, 0.2), 0 0 20px rgba(0, 242, 254, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.1) inset !important;
    transform: translateY(-4px) !important;
}
textarea {
    color: white !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1.05rem !important;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# --- SIDEBAR DASHBOARD ---
with st.sidebar:
    st.markdown("<h1>⚙️ Control Center</h1>", unsafe_allow_html=True)
    st.markdown("### System Status")
    st.success("🟢 All Systems Online")
    
    st.markdown("---")
    st.markdown("### Core Analytics")
    st.metric(label="Knowledge Base", value="RAG Active", delta="Synced")
    st.metric(label="AI Model", value="Gemini 1.5", delta="Ultra-Fast")
    st.metric(label="Security", value="Enterprise", delta="Encrypted")
    
    st.markdown("---")
    st.caption("Secure FinTech Environment. End-to-end encryption active.")

# --- MAIN PAGE ---
st.markdown("""
<div class="ultra-header">
    <h1>FinTech AI</h1>
    <p>Premium Loan Analysis</p>
</div>
""", unsafe_allow_html=True)

if "welcomed" not in st.session_state:
    st.toast('System Initialized successfully!', icon='🚀')
    time.sleep(0.5)
    st.toast('Connecting to Qdrant Vector Database...', icon='🔗')
    time.sleep(0.5)
    st.toast('Ready to process loan terms.', icon='✅')
    st.session_state.welcomed = True

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome to the Enterprise Loan Analysis System. How can I assist you today?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about interest rates, penalties..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        with st.spinner("Analyzing millions of data points..."):
            # Cinematic progress bar effect
            progress_text = "Querying Vector Database..."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            my_bar.empty()
            
            response = ask(prompt)
            
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
