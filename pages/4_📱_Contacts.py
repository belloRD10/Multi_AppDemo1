import streamlit as st

import pandas as pd
from datetime import datetime

st.title("📩 Get in Touch")

st.markdown("We would love to hear from you! Fill out the form below 👇")

# ---------- CONTACT FORM ----------
with st.form("contact_form"):
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email Address")
    message = st.text_area("💬 Your Message")

    submitted = st.form_submit_button("🚀 Send Message")

    if submitted:
        if name and email and message:
            # Save to CSV
            data = {
                "Name": [name],
                "Email": [email],
                "Message": [message],
                "Date": [datetime.now()]
            }
            df = pd.DataFrame(data)

            try:
                df.to_csv("messages.csv", mode="a", header=False, index=False)
            except:
                df.to_csv("messages.csv", index=False)

            st.success(f"✅ Thank you {name}! Your message has been saved.")
        else:
            st.warning("⚠️ Please fill in all fields.")

# ---------- VIEW MESSAGES (ADMIN FEATURE) ----------
st.markdown("---")
if st.checkbox("🔐 Show Submitted Messages (Admin View)"):
    try:
        df = pd.read_csv("messages.csv")
        st.dataframe(df)
    except:
        st.info("No messages yet.")

# ---------- LOCATION MAP ----------
st.markdown("---")
st.subheader("📍 Our Location")

location_data = pd.DataFrame({
    'lat': [12.3615],   # Example: Masbate
    'lon': [123.6200]
})

st.map(location_data)

# ---------- CONTACT INFO ----------
st.markdown("---")
st.subheader("📞 Contact Information")

st.write("📧 Email: bscs@university.edu")
st.write("📱 Phone: +63 912 345 6789")
st.write("🌐 Website: www.bscs-program.edu")

# ---------- SOCIAL MEDIA ----------
st.markdown("---")
st.subheader("🌍 Connect With Us")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("Facebook", "https://facebook.com")

with col2:
    st.link_button("GitHub", "https://github.com")

with col3:
    st.link_button("LinkedIn", "https://linkedin.com")

# ---------- FEEDBACK RATING ----------
st.markdown("---")
st.subheader("⭐ Rate Us")

rating = st.slider("Your Rating", 1, 5)

if rating:
    st.success(f"Thanks for rating us {rating} ⭐!")