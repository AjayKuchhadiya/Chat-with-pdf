import streamlit as st
from modules.data_processing import process_uploaded_files
from modules.rag import generate_response
from search import get_answer

# Initialize Streamlit App
st.title("AI Chat with PDF Knowledge Base")

# Upload PDFs
uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True, type="pdf")
if uploaded_files:
    st.write("Processing uploaded files...")
    for file in uploaded_files:
        process_uploaded_files(file)

# Chat Interface
query = st.text_input("Ask a question about the uploaded PDFs:")
if st.button("Submit"):
    response = get_answer(query)
    st.write("Response:", response)
