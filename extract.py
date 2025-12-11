import pdfplumber


def extract_text_from_pdfs(pdf_files):
    """
    Extracts text from a list of PDF files.

    Args:
    pdf_files (list): List of paths to PDF files.

    Returns:
    list: List of extracted text from each PDF.
    """
    all_texts = []
    for pdf_file in pdf_files:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        all_texts.append(text)
    return all_texts
