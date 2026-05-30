# Medical RAG Chatbot

## Overview

This project lets users upload medical PDFs and ask questions. It retrieves the most relevant document chunks and answers based on the uploaded content.

## Features

- Upload PDF documents
- Extract text from PDF
- Split text into chunks
- Search relevant chunks using TF-IDF similarity
- Answer questions using retrieved context

## Tech Stack

- Python
- Streamlit
- PyPDF
- Scikit-learn

## Resources

- PubMed Central PDFs: https://pmc.ncbi.nlm.nih.gov/
- Streamlit: https://streamlit.io/
- PyPDF: https://pypi.org/project/pypdf/
- Scikit-learn: https://scikit-learn.org/

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Future Improvements

- Add OpenAI/Gemini answer generation
- Add ChromaDB or FAISS vector database
- Add source citations
- Add chat history

## Disclaimer

This project is for educational purposes only and is not medical advice.

## Author

Govardhan Chowdary
