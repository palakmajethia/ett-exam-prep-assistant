import streamlit as st

st.set_page_config(page_title="ExamPrep AI", layout="centered")

st.title("📘 ExamPrep AI")
st.write("Upload your syllabus or notes and generate exam questions.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
