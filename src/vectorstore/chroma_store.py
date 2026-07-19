from langchain_chroma import Chroma

def create_vector_store(documents, embedding_model):

    vector_store = Chroma.from_documents(
        documents = documents,
        embedding = embedding_model,
        persist_directory="chroma_db"
    )

    return vector_store

def load_vector_store(embedding_model):
    
    vector_store= Chroma(
        persist_directory="chroma_db",
        embedding_function= embedding_model
    )

    return vector_store