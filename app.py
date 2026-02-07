import streamlit as st

st.set_page_config(page_title="ExamPrep AI", layout="centered")

st.title("📘 ExamPrep AI")
st.write("Upload your syllabus or notes and generate exam questions.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

question_type = st.selectbox(
    "Select question type",
    ["MCQs", "Short Answers", "Viva Questions"]
)

if st.button("Generate Questions"):
    if uploaded_file is None:
        st.error("Please upload a PDF file")
    else:
        st.success("Processing PDF and generating questions...")
