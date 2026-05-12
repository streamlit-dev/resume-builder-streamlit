import streamlit as st
from fpdf import FPDF
import io

st.title("Resume Builder")

name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
skills = st.text_area("Skills - comma se alag karke likho")
experience = st.text_area("Experience")

if st.button("Resume PDF Banao"):

    if name.strip() and email.strip():

        pdf = FPDF()
        pdf.add_page()

        # Name
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, name, ln=True, align='C')

        # Email & Phone
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Email: {email} | Phone: {phone}", ln=True, align='C')

        pdf.ln(10)

        # Skills
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Skills", ln=True)

        pdf.set_font("Arial", '', 12)

        for skill in skills.split(','):
            if skill.strip():
                pdf.cell(0, 8, f"- {skill.strip()}", ln=True)

        pdf.ln(5)

        # Experience
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Experience", ln=True)

        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 8, experience)

        # PDF ko bytes me convert karo
        pdf_bytes = pdf.output(dest='S').encode('latin-1')

        st.success("PDF Ban Gayi!")

        # Download Button
        st.download_button(
            label="📥 Download Resume PDF",
            data=pdf_bytes,
            file_name="Suman_Resume.pdf",
            mime="application/pdf"
        )

    else:
        st.error("Name aur Email zaruri hai")
