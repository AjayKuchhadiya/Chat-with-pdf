import os
import json
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from modules.store import create_embeddings
from langchain_groq import ChatGroq

METADATA_FILE = "data/metadata.json"

def get_answer(query):
    if not os.path.exists(METADATA_FILE):
        return "No documents have been processed yet."

    with open(METADATA_FILE, "r") as f:
        metadata = json.load(f)

    best_response = None
    highest_score = -1
    source_pdf = None

    # Search across all vector stores
    for pdf_name, vector_store_path in metadata.items():
        vectordb = FAISS.load_local(vector_store_path, embeddings=create_embeddings, allow_dangerous_deserialization=True)
        retrieved_docs = vectordb.similarity_search_with_score(query, k=3)

        for doc, score in retrieved_docs:
            if score > highest_score:
                highest_score = score
                best_response = doc.page_content
                source_pdf = pdf_name

    if best_response is None:
        return "No relevant document found for this query."

    return f"Answer: {best_response}\n(Source: {source_pdf})"
