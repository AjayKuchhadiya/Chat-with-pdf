# AI Chat with Multi-PDF Knowledge Base

This application allows users to upload PDF files, process them into a searchable database, and interact with an AI chatbot to query information from the uploaded documents.

## Features

- **PDF Upload**: Upload multiple PDF files for processing.
- **OCR Support**: Extracts text from both text-based and image-based PDFs using OCR (Tesseract).
- **AI-Powered Search**: Query the content of the uploaded documents using an AI chatbot.
- **Embeddings with Gemini**: Uses Google Gemini embeddings for document vectorization.
- **Vector Store**: Stores processed document data in a FAISS vector database.

## Tech Stack

- **Backend**: Python with Flask and Streamlit
- **AI Models**: Google Gemini and GroqChat
- **Database**: FAISS Vector Store
- **OCR**: Tesseract via PyMuPDF and PIL
- **Frontend**: Streamlit for user interaction

## Prerequisites

1. Python 3.10 or above
2. Install Tesseract OCR (for image-based PDF processing):
   - On Ubuntu: `sudo apt install tesseract-ocr`
   - On Windows: [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)

## How to Run

1. **Clone the repository and setup dependencies**:
   ```bash
   git clone https://github.com/AjayKuchhadiya/Chat-with-pdf/
   cd Chat-With-Pdf
   venv/scripts/activate
   pip install -r requirements.txt
   ```

2. **Environment setup**:
   - Create a `.env` file with the following variables:
     ```
     GOOGLE_API_KEY=<your_google_api_key>
     GROQ_API_KEY=<your_groq_api_key>
     ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**:
   - Open your browser and navigate to `http://localhost:8501`.


## Important Notes

1. **Data Cleanup**: Uploaded files and vector database are cleared whenever new documents are processed or the app restarts.

