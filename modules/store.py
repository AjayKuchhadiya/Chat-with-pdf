import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from langchain.schema import Document

load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(text):
    return model.encode(text)

def read_pdf_with_ocr(pdf_path):
    doc = fitz.open(pdf_path)
    text_content = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        if text.strip():
            text_content.append(text)
        else:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            ocr_text = pytesseract.image_to_string(img)
            text_content.append(ocr_text)

    doc.close()
    return "\n".join(text_content)

def create_db(pdf_path):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    folder_name = f"data/db_{pdf_name}"
    os.makedirs(folder_name, exist_ok=True)

    content = read_pdf_with_ocr(pdf_path)
    documents = [Document(page_content=content, metadata={"source": pdf_name})]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    for text in texts:
        text.metadata["source"] = pdf_name

    text_embeddings = [(text.page_content, create_embeddings(text.page_content)) for text in texts]
    vectordb = FAISS.from_embeddings(text_embeddings=text_embeddings, embedding=create_embeddings)
    vectordb.save_local(folder_name)

    return folder_name
