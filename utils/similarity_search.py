from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(text, doc_id):
    embedding = model.encode(text)
    return embedding

def retrieve_relevant_chunks(query, embeddings, top_k=3):
    query_embedding = model.encode(query)
    similarities = {doc_id: util.pytorch_cos_sim(query_embedding, emb)[0][0] for doc_id, emb in embeddings.items()}
    sorted_docs = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:top_k]
    
    relevant_chunks = [embeddings[doc_id]['text'] for doc_id, _ in sorted_docs]
    print('relevant_chunks \n', relevant_chunks)
    return relevant_chunks

