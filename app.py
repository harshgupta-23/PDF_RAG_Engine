import os
import time

import streamlit as st

from extract import extract_text_from_pdfs
from generate import generate_response
from preprocess import preprocess_text
from retrieve import create_vectorizer, retrieve

# Streamlit UI
st.title("RAG-based PDF Query System")

uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write("Processing the uploaded PDFs...")

    # Initialize progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Save uploaded files to disk
    pdf_files = []
    for uploaded_file in uploaded_files:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        pdf_files.append(uploaded_file.name)

    # Extract text from PDFs with progress updates
    num_files = len(pdf_files)
    texts = []
    for i, pdf_file in enumerate(pdf_files):
        status_text.text(f"Extracting text from file {i + 1} of {num_files}...")
        text = extract_text_from_pdfs([pdf_file])
        texts.extend(text)
        progress_bar.progress((i + 1) / num_files)
        time.sleep(0.1)  # Simulate time taken for processing

    # Preprocess text with progress updates
    status_text.text("Preprocessing text...")
    progress_bar.progress(0.5)
    processed_texts = preprocess_text(texts)
    time.sleep(0.1)  # Simulate time taken for processing

    # Create vectorizer and transform texts
    status_text.text("Creating vectorizer and transforming texts...")
    progress_bar.progress(0.75)
    vectorizer, X = create_vectorizer(processed_texts)
    time.sleep(0.1)  # Simulate time taken for processing

    # Finalize progress
    progress_bar.progress(1.0)
    status_text.text("Processing complete!")

    query = st.text_input("Enter your query:")

    if query:
        # Retrieve relevant texts
        top_indices = retrieve(query, X, vectorizer)
        retrieved_texts = [texts[i] for i in top_indices]

        # Generate response
        response = generate_response(retrieved_texts, query)

        st.write("Response:")
        st.write(response)

    # Clean up uploaded files
    for pdf_file in pdf_files:
        os.remove(pdf_file)
