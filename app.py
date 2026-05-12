import streamlit as st
from fpdf import FPDF2

st.title("Resume Builder App")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
skills = st.text_area("Skills - comma se alag karein")
experience = st.text_area("Work Experience")
education = st.text_area("Education")

if st.button("Resume PDF Banao"):
    if name.strip() and email.strip():
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, name, ln=True, align='C')
        
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Email: {email} | Phone: {phone}", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Skills", ln=True)
        pdf.set_font("Arial", '', 12)
        for skill in skills.split(','):
            pdf.cell(0, 8, f"- {skill.strip()}", ln=True)
        pdf.ln(5)
        
       pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Experience", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8, experience)
pdf.ln(5)

pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Education", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8, education)

pdf_data = pdf.output(dest='S').encode('latin-1')
st.download_button(label="Download PDF", data=pdf_data, file_name="resume.pdf")
