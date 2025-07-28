import streamlit as st

def home():
    st.set_page_config(page_title="Skin Cancer Detection", layout="wide")
    
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #555;
        }
        .info-box {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .button-style {
            display: inline-block;
            padding: 0.75rem 1.25rem;
            background-color: #0066cc;
            color: white;
            border: none;
            border-radius: 10px;
            text-align: center;
            font-size: 1rem;
            margin-top: 10px;
            width: 100%;
        }
        .button-style:hover {
            background-color: #0055aa;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title section
    st.markdown('<div class="main-title">🧬 AI-Powered Skin Cancer Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your smart assistant for early skin cancer screening and awareness.</div>', unsafe_allow_html=True)

    # Optional: Uncomment if you have a banner
    # st.image("assets/skin_cancer_banner.jpg", use_container_width=True)

    # Feature overview
    st.markdown("""<div class="info-box">
    <ul>
        <li>📤 Upload a skin lesion image to get an AI-powered diagnosis.</li>
        <li>👨‍🔬 Learn about our expert team and the deep learning technology behind the system.</li>
        <li>🤖 Use the integrated chatbot for quick FAQs and user support.</li>
    </ul>
    </div>""", unsafe_allow_html=True)

    # Navigation Buttons
    st.markdown("#### 👉 What would you like to do?")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔍 Predict Skin Cancer", use_container_width=True):
            st.session_state["page"] = "predict_skin_cancer"

    with col2:
        if st.button("💬 Chat with AI", use_container_width=True):
            st.session_state["page"] = "chat_page"

    with col3:
        if st.button("👩‍💼 Meet the Team", use_container_width=True):
            st.session_state["page"] = "team_members"

if __name__ == "__main__":
    home()
