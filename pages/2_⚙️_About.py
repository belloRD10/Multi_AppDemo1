import streamlit as st

st.title("📘 About the BSCS Program")

tab1, tab2, tab3 = st.tabs(["Overview", "Skills", "Career Paths"])

with tab1:
    st.write("""
    The BSCS program focuses on computation, algorithms, and system design.
    Students learn both theoretical foundations and practical applications.
    """)

with tab2:
    skills = {
        "Programming": 90,
        "Problem Solving": 85,
        "Data Structures": 80,
        "AI & ML": 75
    }
    for skill, val in skills.items():
        st.write(skill)
        st.progress(val)

with tab3:
    career = st.selectbox("Select a Career", ["Software Developer", "Data Scientist", "Cybersecurity Analyst", "AI Engineer"])
    st.success(f"You selected: {career}")