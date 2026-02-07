import streamlit as st

# Backend function imports (assumed to exist)
from backend.rag_pipeline import (
    load_pdf,
    chunk_text,
    retrieve_relevant_chunks,
    generate_mcqs,
    generate_short_questions,
    generate_viva_questions
)

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
        text = load_pdf(uploaded_file)
        chunks = chunk_text(text)
        context = retrieve_relevant_chunks(chunks)

        if question_type == "MCQs":
            questions = generate_mcqs(context)
        elif question_type == "Short Answers":
            questions = generate_short_questions(context)
        else:
            questions = generate_viva_questions(context)

        st.subheader("Generated Questions")
        for i, q in enumerate(questions, 1):
            st.write(f"{i}. {q}")
