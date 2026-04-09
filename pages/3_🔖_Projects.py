import streamlit as st

import random

st.title("🧪 Student Projects Showcase")

st.markdown("### 🎮 Project Idea Generator")
ideas = [
    "AI Chatbot",
    "Online Voting System",
    "E-Commerce Platform",
    "Face Recognition System",
    "Smart Attendance System"
]

if st.button("Generate Project Idea"):
    st.success(random.choice(ideas))

st.markdown("---")

st.markdown("### 📊 Mini Data Visualizer")
numbers = st.slider("Select range", 1, 100, 50)
data = list(range(numbers))
st.line_chart(data)

st.markdown("---")

st.markdown("### 🧠 Coding Challenge")

# List of questions and answers
questions = [
    {"question": "What is 2 + 2 * 2?", "answer": "6"},
    {"question": "What is 10 / 2 + 3?", "answer": "8"},
    {"question": "What is 5 * 3 - 4?", "answer": "11"},
    {"question": "What is 9 + 1 * 0?", "answer": "9"},
    {"question": "What is (6 + 2) * 2?", "answer": "16"}
]

# Initialize session state
if "current_q" not in st.session_state:
    st.session_state.current_q = random.choice(questions)

# Display question
st.write(st.session_state.current_q["question"])

# User input
answer = st.text_input("Your Answer:")

# Check answer
if answer:
    if answer.strip() == st.session_state.current_q["answer"]:
        st.success("✅ Correct!")

        # Generate new question after correct answer
        if st.button("Next Question"):
            st.session_state.current_q = random.choice(questions)
            st.rerun()
    else:
        st.error("❌ Try again!")
