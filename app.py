import gradio as gr
from agent import ask

def chat_wrapper(user_msg, chat_history):
    bot_msg = ask(user_msg)
    chat_history.append({"role": "user", "content": user_msg})
    chat_history.append({"role": "assistant", "content": bot_msg})
    return "", chat_history

custom_css = """
/* Ultimate Premium FinTech Holographic Theme */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&display=swap');

body {
    background: linear-gradient(-45deg, #0f172a, #1e1b4b, #000000, #312e81) !important;
    background-size: 400% 400% !important;
    animation: gradientBG 15s ease infinite !important;
    font-family: 'Space Grotesk', sans-serif !important;
    color: white !important;
    margin: 0;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Glassmorphism Wrapper with Neon Glow */
.glass-wrapper {
    background: rgba(255, 255, 255, 0.02) !important;
    backdrop-filter: blur(25px) saturate(150%) !important;
    -webkit-backdrop-filter: blur(25px) saturate(150%) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 30px !important;
    padding: 30px !important;
    box-shadow: 0 0 50px rgba(99, 102, 241, 0.2), inset 0 0 20px rgba(255, 255, 255, 0.05) !important;
    margin-top: 30px;
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
    font-size: 3.5rem;
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
    font-size: 1.3rem;
    font-weight: 300;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Chatbot Styling & Scrollbar */
.chatbot-container {
    border: none !important;
    background: transparent !important;
}
.chatbot-container::-webkit-scrollbar {
    width: 8px;
}
.chatbot-container::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05); 
    border-radius: 10px;
}
.chatbot-container::-webkit-scrollbar-thumb {
    background: rgba(99, 102, 241, 0.5); 
    border-radius: 10px;
}

/* Textbox with Animated Neon Border */
.custom-textbox textarea {
    background: rgba(0, 0, 0, 0.4) !important;
    border: 2px solid transparent !important;
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), linear-gradient(90deg, #00f2fe, #4facfe) !important;
    background-origin: border-box !important;
    background-clip: padding-box, border-box !important;
    color: white !important;
    border-radius: 20px !important;
    padding: 20px !important;
    font-size: 1.2rem !important;
    transition: all 0.3s ease !important;
}
.custom-textbox textarea:focus {
    box-shadow: 0 0 30px rgba(0, 242, 254, 0.4) !important;
}

/* 3D Submit Button */
.custom-btn {
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%) !important;
    border: none !important;
    border-radius: 20px !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 1.3rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    box-shadow: 0 10px 20px rgba(0, 242, 254, 0.3), inset 0 -3px 0 rgba(0,0,0,0.2) !important;
}
.custom-btn:hover {
    transform: translateY(-5px) scale(1.05) !important;
    box-shadow: 0 15px 30px rgba(0, 242, 254, 0.5), inset 0 -3px 0 rgba(0,0,0,0.2) !important;
}
.custom-btn:active {
    transform: translateY(2px) !important;
    box-shadow: 0 5px 10px rgba(0, 242, 254, 0.3) !important;
}
"""

with gr.Blocks(title="FinTech AI Engine") as demo:
    gr.HTML("""
        <div class="premium-header">
            <h1>🏦 FinTech AI Engine</h1>
            <p>Enterprise-grade Loan Term Analysis & Intelligent Retrieval</p>
        </div>
    """)
    
    with gr.Column(elem_classes="glass-wrapper"):
        chatbot = gr.Chatbot(
            height=500,
            elem_classes="chatbot-container",
            avatar_images=("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", "https://cdn-icons-png.flaticon.com/512/6894/6894344.png"),
            show_label=False
        )
        
        with gr.Row():
            msg = gr.Textbox(
                placeholder="Ask about interest rates, penalties, or payment terms...", 
                container=False, 
                scale=8,
                elem_classes="custom-textbox"
            )
            submit = gr.Button("Send 🚀", elem_classes="custom-btn", scale=1)

        gr.Examples(
            examples=[
                "What happens if I miss a payment?",
                "Tell me about the interest rate.",
                "Are there any penalties for early repayment?"
            ],
            inputs=msg
        )

    msg.submit(chat_wrapper, [msg, chatbot], [msg, chatbot])
    submit.click(chat_wrapper, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port, css=custom_css)
