import fitz  # PyMuPDF

def load_pdf_content(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text
