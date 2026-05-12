import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

st.title("Resume Builder")

name = st.text_input("Name")
email = st.text_input("Email") 
phone = st.text_input("Phone")
skills = st.text_area("Skills - comma se alag karke likho")
experience = st.text_area("Experience")

if st.button("Resume PDF Banao"):
    if name.strip() and email.strip():
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        
        y = height - 50  # Upar se start
        
        # Name
        p.setFont("Helvetica-Bold", 18)
        p.drawCentredString(width/2, y, name)
        y -= 30
        
        # Email Phone
        p.setFont("Helvetica", 12)
        p.drawCentredString(width/2, y, f"Email: {email} | Phone: {phone}")
        y -= 40
        
        # Skills
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "Skills:")
        y -= 20
        p.setFont("Helvetica", 12)
        for skill in skills.split(','):
            if skill.strip():
                p.drawString(70, y, f"- {skill.strip()}")
                y -= 15
        y -= 10
        
        # Experience
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "Experience:")
        y -= 20
        p.setFont("Helvetica", 12)
        for line in experience.split('\n'):
            p.drawString(70, y, line)
            y -= 15
        
        p.save()
        buffer.seek(0)
        
        st.success("PDF Ban Gayi! ✅")
        st.download_button(
            label="📥 Download Resume PDF",
            data=buffer,
            file_name="resume.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Name aur Email zaruri hai")
        
