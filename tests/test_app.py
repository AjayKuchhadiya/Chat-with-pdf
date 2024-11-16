import os
from modules.data_processing import process_uploaded_files
from modules.store import create_db, read_pdf_with_ocr
from modules.search import get_answer

# Define the paths for test PDFs and test directories
TEST_DATA_DIR = "tests/test_data"
UPLOADS_DIR = "data/uploads"
DB_PATH = "db"


def test_process_uploaded_files():
    """Test processing of uploaded files."""
    # Clear the uploads directory
    if os.path.exists(UPLOADS_DIR):
        for f in os.listdir(UPLOADS_DIR):
            os.remove(os.path.join(UPLOADS_DIR, f))

    # Load test files
    test_files = [
        open(os.path.join(TEST_DATA_DIR, "test1.pdf"), "rb"),
        open(os.path.join(TEST_DATA_DIR, "test2.pdf"), "rb"),
    ]
    
    # Mimic Streamlit uploaded files structure
    class UploadedFile:
        def __init__(self, name, content):
            self.name = name
            self.content = content
        
        def getbuffer(self):
            return self.content

    uploaded_files = [
        UploadedFile("test1.pdf", test_files[0].read()),
        UploadedFile("test2.pdf", test_files[1].read()),
    ]

    # Process files
    process_uploaded_files(uploaded_files)

    # Check that files are saved correctly
    for file in uploaded_files:
        file_path = os.path.join(UPLOADS_DIR, file.name)
        assert os.path.exists(file_path)

    # Clean up
    for f in test_files:
        f.close()


def test_read_pdf_with_ocr():
    """Test reading PDFs with OCR."""
    test_pdf_path = os.path.join(TEST_DATA_DIR, "test2.pdf")
    text = read_pdf_with_ocr(test_pdf_path)
    assert text.strip() != ""  # Ensure that text was extracted


def test_create_db():
    """Test database creation from uploaded files."""
    # Ensure the uploads directory exists
    os.makedirs(UPLOADS_DIR, exist_ok=True)

    # Copy test PDFs to the uploads directory
    test_files = ["test1.pdf", "test2.pdf"]
    for file_name in test_files:
        src_path = os.path.join(TEST_DATA_DIR, file_name)
        dest_path = os.path.join(UPLOADS_DIR, file_name)
        with open(src_path, "rb") as src, open(dest_path, "wb") as dest:
            dest.write(src.read())

    # Create the database
    create_db(UPLOADS_DIR)

    # Check that the FAISS database exists
    assert os.path.exists(DB_PATH)


def test_get_answer():
    """Test retrieval and question-answering functionality."""
    query = "What is the content of the uploaded PDF?"
    
    # Ensure the database exists
    if not os.path.exists(DB_PATH):
        test_create_db()

    # Test the answer retrieval
    response = get_answer(query)
    assert response.strip() != ""  # Ensure a response is returned
