from src.embeddings.embedding_model import get_embedding_model
from src.vectorstore.chroma_store import load_vector_store


def main():

    print("=" * 70)
    print("Enterprise Agentic RAG Chat")
    print("Type 'exit' to quit.")
    print("=" * 70)

    # Load embedding model
    embedding_model = get_embedding_model()

    # Load existing Chroma vector database
    vector_store = load_vector_store(embedding_model)

    print("\n Vector Store loaded successfully.\n")

    while True:

        question = input("Ask a question: ")

        if question.lower() == "exit":
            print("\nGoodbye!\n")
            break

        # Retrieve top 3 similar documents
        results = vector_store.similarity_search(
            query=question,
            k=3
        )

        print("\n" + "=" * 70)
        print(f"Top {len(results)} Retrieved Documents")
        print("=" * 70)

        for i, doc in enumerate(results, start=1):

            print(f"\nResult {i}")
            print("-" * 70)

            print(doc.page_content)

            print("\nMetadata")
            print(doc.metadata)

        print("\n")


if __name__ == "__main__":
    main()