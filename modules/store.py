from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader  # Updated import paths
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

# Initialize the SentenceTransformer model for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Define a function to create embeddings using SentenceTransformer
def create_embeddings(text):
    return model.encode(text)

def create_db(file_path): 
    # Load and process the PDF files
    loader = DirectoryLoader(file_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    # Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    # Generate tuples of (text content, embedding) for each text chunk
    text_embeddings = [(text.page_content, create_embeddings(text.page_content)) for text in texts]
    
    # Create FAISS vector store using the text embeddings and the original text chunks
    vectordb = FAISS.from_embeddings(text_embeddings=text_embeddings, embedding=create_embeddings)

    # Save the vector store locally
    vectordb.save_local("db")
