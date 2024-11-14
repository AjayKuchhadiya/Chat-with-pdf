from utils.similarity_search import retrieve_relevant_chunks
from modules.llm import get_answer
from modules.data_processing import all_embeddings

def generate_response(query):
    # Retrieve similar content from the PDFs
    print('all_embeddings \n', all_embeddings)
    relevant_text_chunks = retrieve_relevant_chunks(query, all_embeddings)
    # Combine query and relevant text for LLM input
    print('relevant_chunks : \n\n',relevant_text_chunks)
    response = get_answer(relevant_text_chunks, query)
    return response
