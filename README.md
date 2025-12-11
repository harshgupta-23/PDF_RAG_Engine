# RAG-based PDF Query System

**Chat with your documents!** This project implements a **Retrieval-Augmented Generation (RAG)** system built on Streamlit that allows users to upload multiple PDF files and query their contents using the power of OpenAI's GPT-3.5-turbo.

It transforms static documents into a dynamic, searchable knowledge base, providing **accurate** and **context-aware** answers grounded entirely in your uploaded files.

---

## Features and Capabilities

* **Multi-PDF Support:** Upload and merge knowledge from multiple PDF documents into a single knowledge base.
* **Accurate Extraction:** Uses `pdfplumber` for robust and accurate text extraction, even from complex PDF layouts.
* **Context-Aware AI:** Leverages the RAG technique to retrieve the most relevant text chunks (using **TF-IDF** and **Cosine Similarity**) before generating a response with the **OpenAI GPT-3.5-turbo** model.
* **Interactive Web App:** Powered by **Streamlit** for an easy-to-use, real-time feedback interface.
* **Secure API Handling:** Uses a `.env` file to securely manage your OpenAI API Key.

---

## Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend/App** | `Streamlit` | Interactive web application and user interface. |
| **Text Extraction** | `pdfplumber` | Accurate retrieval of text from PDF files. |
| **NLP & Preprocessing** | `NLTK` | Tokenization and cleaning of extracted text. |
| **Vectorization/Retrieval** | `Scikit-learn` | TF-IDF Vectorization and Cosine Similarity for fast retrieval. |
| **Generative Model** | `OpenAI GPT-3.5-turbo` | Generating grounded, natural-language answers. |

---

## Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

* **Python:** Version 3.7 or higher.
* **OpenAI API Key:** Required to use the GPT-3.5-turbo model. Get one from the [OpenAI website](https://beta.openai.com/signup/).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/harshgupta-23/PDF_RAG_Engine.git
    cd PDF_RAG_Engine
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Linux/macOS
    # env\Scripts\activate   # On Windows
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download NLTK data:**
    ```python
    python -c "import nltk; nltk.download('punkt')"
    ```

5.  **Configure API Key:**
    * Create a file named **`.env`** in the project's root directory.
    * Add your API key inside this file.

    ```text
    # .env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Running the Application

1.  **Start the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2.  **Access:** Open your web browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`).

### How to Use

1.  Use the sidebar to **upload one or more PDF files**.
2.  Wait briefly for the progress bar to complete the text extraction and knowledge base creation.
3.  Enter your question into the chat box.
4.  The system will instantly retrieve relevant text and use it to formulate a precise answer.

---

## Notes

* Ensure your `.env` file is protected and your API key is correct.
* A stable internet connection is required for the application to communicate with the OpenAI API.
* This project is excellent for use cases like querying technical manuals, financial reports, or large academic papers.
