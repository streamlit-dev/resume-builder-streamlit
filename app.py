import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])

import streamlit as st
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

st.title("Resume Builder - Works 100%")
st.write("Bhai ye final version hai")

name = st.text_input("Name")
email = st.text_input("Email") 
phone = st.text_input("Phone")
skills = st.text_area("Skills - comma se alag karke likho")
experience = st.text_area("Experience")

if st.button("PDF Banao"):
    if name and email:
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, f"Name: {name}")
        p.drawString(100, 730, f"Email: {email}")
        p.drawString(100, 710, f"Phone: {phone}")
        p.drawString(100, 690, f"Skills: {skills}")
        p.drawString(100, 670, f"Experience: {experience}")
        p.save()
        buffer.seek(0)
        
        st.success("Ban Gayi PDF!")
        st.download_button("Download PDF", buffer, "resume.pdf")
    else:
        st.error("Name Email bhar bhai")
        st.error("Name Email bhar bhai")
        
