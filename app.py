import streamlit as st

# ===== Assume backend functions exist =====
from src.backend import (
    load_pdf,
    chunk_text,
    retrieve_relevant_chunks,
    generate_mcqs,
    generate_short_questions,
    generate_viva_questions
)

# ===== Page Config =====
st.set_page_config(
    page_title="ExamPrep AI",
    layout="centered"
)

st.title("📘 ExamPrep AI")
st.subheader("Upload your syllabus / notes and generate exam questions")

# ===== File Upload =====
uploaded_file = st.file_uploader(
    "Upload PDF file",
    type=["pdf"]
)

# ===== Question Type Selection =====
question_type = st.selectbox(
    "Select question type",
    ["MCQs", "Short Answer", "Viva Questions"]
)

# ===== Generate Button =====
if st.button("Generate Questions"):

    if uploaded_file is None:
        st.error("❌ Please upload a PDF file first")
    
    else:
        with st.spinner("Processing document..."):
            # Save file temporarily
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

            # Backend pipeline (already handled by teammate)
            text = load_pdf("temp.pdf")
            chunks = chunk_text(text)
            context = retrieve_relevant_chunks(chunks)

            # Question generation
            if question_type == "MCQs":
                output = generate_mcqs(context)

            elif question_type == "Short Answer":
                output = generate_short_questions(context)

            else:
                output = generate_viva_questions(context)

        # ===== Output Display =====
        st.success("✅ Questions generated successfully")
        st.write(output)
