import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])

import streamlit as st
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

st.title("Resume Builder")

name = st.text_input("Name")
email = st.text_input("Email") 
phone = st.text_input("Phone")
skills = st.text_area("Skills - comma se alag karke likho")
experience = st.text_area("Experience")

if st.button("PDF Banao"):
    if name and email:
        try:
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            p.drawString(100, 750, f"Name: {name}")
            p.drawString(100, 730, f"Email: {email}")
            p.drawString(100, 710, f"Phone: {phone}")
            p.drawString(100, 690, f"Skills: {skills}")
            p.drawString(100, 650, f"Experience: {experience}")
            p.save()
            buffer.seek(0)
            
            st.success("Ban Gayi PDF! Neeche Download Kar")
            
            # YE LINE SABSE IMPORTANT HAI - MIME TYPE ADD KIYA
            st.download_button(
                label="📥 Download Resume PDF",
                data=buffer,
                file_name="resume.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"Error: {e}")
            st.write("Error ka detail:", e)
    else:
        st.error("Name Email bhar bhai")
        st.error("Name Email bhar bhai")
        
