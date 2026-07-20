from src.loaders.pdf_loader import load_pdf
from src.chunking.text_splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model
from sklearn.metrics.pairwise import cosine_similarity
from src.vectorstore.chroma_store import create_vector_store
from src.vectorstore.chroma_store import load_vector_store

def main():

    print("Loading documents...")

    documents = load_pdf("data/employee_handbook.pdf")

    print(f"Loaded {len(documents)} pages.")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    embedding_model = get_embedding_model()

    create_vector_store(
        chunks,
        embedding_model
    )

    print("Vector database created successfully.")


if __name__ == "__main__":
    main()

