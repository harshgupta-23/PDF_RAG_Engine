import pdfplumber
from typing import List

def extract_text_from_pdfs(pdf_files: List[str]) -> List[str]:
    """
    Extracts text from PDF files with basic error handling.
    """
    all_texts = []
    for pdf_file in pdf_files:
        try:
            with pdfplumber.open(pdf_file) as pdf:
                # Use join for better performance in large documents
                text = " ".join(page.extract_text() or "" for page in pdf.pages)
                all_texts.append(text)
        except Exception as e:
            print(f"Error extracting {pdf_file}: {e}")
            all_texts.append("")
    return all_texts
