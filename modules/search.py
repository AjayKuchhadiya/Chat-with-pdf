from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from modules.store import create_embeddings  
from dotenv import load_dotenv

load_dotenv()

def get_answer(query): 
    
    # Load the FAISS vector store using SentenceTransformer embeddings
    vectordb = FAISS.load_local("db", embeddings=create_embeddings, allow_dangerous_deserialization=True)

    # Make the retriever
    retriever = vectordb.as_retriever(search_kwargs={"k": 10}, search_type="mmr")  

    groq = ChatGroq(temperature=0, model_name="llama3-8b-8192")

    qa_chain = RetrievalQA.from_chain_type(
        llm=groq,
        chain_type="stuff",
        retriever=retriever
    )


    llm_response = qa_chain(query)
    print('llm_response: \n', llm_response)
    return llm_response['result']