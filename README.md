# RAG-based PDF Query System

This project implements a Retrieval-Augmented Generation (RAG) system that allows users to upload multiple PDF files, extract and preprocess the text, and then query the contents of those PDFs using OpenAI's GPT-3.5-turbo model. The system combines the strengths of information retrieval and text generation to provide accurate and context-aware responses to user queries.

## Description

The RAG-based PDF Query System is designed to:
1. **Extract Text from PDFs:** Utilize `pdfplumber` to accurately extract text from multiple PDF files.
2. **Preprocess Text:** Clean and tokenize the extracted text for better processing.
3. **Create a Knowledge Base:** Use TF-IDF vectorization to create a searchable knowledge base from the extracted text.
4. **Retrieve Relevant Texts:** Retrieve the most relevant texts based on the user query using cosine similarity.
5. **Generate Responses:** Use OpenAI's GPT-3.5-turbo model to generate responses based on the retrieved texts and user query.

### Key Components and Technologies Used

- **Streamlit:** For building an interactive web application.
- **pdfplumber:** For extracting text from PDF files.
- **NLTK:** For text preprocessing tasks such as tokenization.
- **Scikit-learn:** For TF-IDF vectorization and text retrieval.
- **OpenAI GPT-3.5-turbo:** For generating context-aware responses to user queries.

### Why This Project?

- **Combining Retrieval and Generation:** The project combines information retrieval with advanced text generation, providing users with accurate and context-aware responses.
- **Interactive Interface:** Streamlit offers an easy-to-use interface for uploading PDFs and querying their contents.
- **Advanced Text Extraction:** `pdfplumber` ensures accurate extraction of text from PDFs, even from complex layouts.
- **State-of-the-art Language Model:** OpenAI's GPT-3.5-turbo is one of the most advanced language models, ensuring high-quality responses.

## How to Run

### Prerequisites

- Python 3.7 or higher
- OpenAI API Key (you can get it from the [OpenAI website](https://beta.openai.com/signup/))

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/rag-pdf-query-system.git
    cd rag-pdf-query-system
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK data:**
    ```python
    import nltk
    nltk.download('punkt')
    ```

5. **Create a `.env` file in the project root directory:**
    ```text
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Running the Application

1. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2. **Use the Application:**
    - Open the URL provided by Streamlit (usually `http://localhost:8501`) in your web browser.
    - Upload one or more PDF files.
    - Enter your query in the input box.
    - View the generated response based on the contents of the uploaded PDFs.

### Notes

- The progress bar in the Streamlit application provides real-time feedback during the PDF processing stages.
- Ensure you have a stable internet connection to interact with the OpenAI API for generating responses.

This project demonstrates the integration of various tools and libraries to create a powerful and interactive query system for PDF documents.
