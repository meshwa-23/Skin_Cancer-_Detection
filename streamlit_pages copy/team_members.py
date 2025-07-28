import streamlit as st

def team():
    st.set_page_config(page_title="Meet the Team", layout="wide")

    # Inject custom CSS
    st.markdown("""
        <style>
        .title {
            font-size: 2.5rem;
            color: #2c3e50;
            font-weight: 700;
        }

        .subtitle {
            font-size: 1.1rem;
            color: #555;
            margin-bottom: 30px;
        }

        .team-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 30px;
        }

        .team-card {
            background: linear-gradient(135deg, #e0f7fa, #e3f2fd);
            border-radius: 15px;
            padding: 25px;
            width: 220px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            transition: transform 0.3s ease;
        }

        .team-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 28px rgba(0,0,0,0.25);
        }

        .team-name {
            font-size: 1.3rem;
            font-weight: bold;
            color: #1a237e;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown('<div class="title">👩‍🔬 Meet the Team</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Our passionate team is committed to building intelligent solutions for early skin cancer detection.</div>', unsafe_allow_html=True)

    # Team members list
    team_members = [
        "Ankit Pattanaik",
        "Anubhab B",
        "Sakshi Singh",
        "Prerna",
        "Meshwa Hirpara"
    ]

    # Layout team cards
    st.markdown('<div class="team-container">', unsafe_allow_html=True)
    for member in team_members:
        st.markdown(f"""
            <div class="team-card">
                <div class="team-name">{member}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    team()
