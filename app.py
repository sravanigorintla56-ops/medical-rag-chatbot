import streamlit as st
from pdf_utils import extract_text_from_pdf, split_text
from retriever import retrieve_relevant_chunks

st.set_page_config(page_title="Medical RAG Chatbot", layout="wide")

st.title("Medical RAG Chatbot")
st.write("Upload a medical PDF and ask questions based on the document.")

uploaded_file = st.file_uploader("Upload Medical PDF", type=["pdf"])
question = st.text_input("Ask a question")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    chunks = split_text(text)
    st.success(f"PDF processed successfully. Total chunks: {len(chunks)}")

    if st.button("Get Answer"):
        if not question.strip():
            st.error("Please enter a question.")
        else:
            relevant_chunks = retrieve_relevant_chunks(question, chunks)
            st.subheader("Most Relevant Context")
            for i, chunk in enumerate(relevant_chunks, start=1):
                st.write(f"### Context {i}")
                st.write(chunk)

            st.info("This starter version retrieves context. Add OpenAI/Gemini to generate final answers.")
