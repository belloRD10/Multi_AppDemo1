import streamlit as st
import datetime
import random

st.set_page_config(page_title="BSCS Experience Hub", page_icon="💻", layout="wide")

st.title("💻 Bachelor of Science in Computer Science")
st.subheader("Welcome to the Future of Innovation 🚀")

st.markdown("""
The **BSCS program** equips students with the knowledge and skills needed to design, develop, and innovate software solutions.
From algorithms to artificial intelligence, this course builds the backbone of modern technology.
""")

col1, col2 = st.columns(2)

with col1:
    st.info("📊 Fun Fact Generator")
    facts = [
        "Over 90% of innovations today rely on Computer Science.",
        "Python is one of the most popular programming languages.",
        "AI is transforming industries worldwide.",
        "Cybersecurity jobs are rapidly increasing globally."
    ]
    if st.button("Generate Fun Fact"):
        st.success(random.choice(facts))

with col2:
    st.info("⏰ Real-Time Clock")
    now = datetime.datetime.now()
    st.write("Current Date & Time:")
    st.code(now.strftime("%Y-%m-%d %H:%M:%S"))

st.markdown("---")
st.subheader("🎯 Why Choose BSCS?")
st.progress(85)
st.write("Industry Demand Level")