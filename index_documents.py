from src.loaders.pdf_loader import load_pdf
from src.chunking.text_splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model
from sklearn.metrics.pairwise import cosine_similarity
from src.vectorstore.chroma_store import create_vector_store
from src.vectorstore.chroma_store import load_vector_store

def main():

    #documents = load_pdf("data/employee_handbook.pdf")

    # print("=" * 60)
    # print(f"Total Documents : {len(documents)}")
    # print("=" * 60)

    # chunks = split_documents(documents)
    # print(f"Total Chunks {len(chunks)}") 
    # print("=" * 60)

    embedding_model = get_embedding_model()

    #vector_store = create_vector_store(chunks, embedding_model)
    vector_store = load_vector_store(embedding_model)

    print("Vector Store Create Successfully ")

    results = vector_store.similarity_search(
        "How many casual leaves do employees receive?",
        k=3
    )

    print(type(results))
    print(len(results))
    print(type(results[0]))
    print(results[0])

    



    


if __name__ == "__main__":
    main()