from src.embeddings.embedding_model import get_embedding_model
from src.vectorstore.chroma_store import load_vector_store
from src.prompts.prompt_template import RAG_PROMPT
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

def main():
    load_dotenv()

    print("=" * 70)
    print("Enterprise Agentic RAG Chat")
    print("Type 'exit' to quit.")
    print("=" * 70)

    # Load embedding model
    embedding_model = get_embedding_model()

    # Load existing Chroma vector database
    vector_store = load_vector_store(embedding_model)

    print("\n Vector Store loaded successfully.\n")

    question = input("Ask a question: ")

    documents = vector_store.similarity_search(question, k=3)

    context = "\n\n".join( doc.page_content for doc in documents)
    

    formatted_prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    #print(formatted_prompt)

    llm= ChatOpenAI(
        model= "gpt-4o-mini",
        temperature=0
    )

    response = llm.invoke(formatted_prompt)

    print(response.content)



    # while True:

    #     question = input("Ask a question: ")

    #     if question.lower() == "exit":
    #         print("\nGoodbye!\n")
    #         break

    #     # Retrieve top 3 similar documents
    #     results = vector_store.similarity_search(
    #         query=question,
    #         k=3
    #     )

    #     print("\n" + "=" * 70)
    #     print(f"Top {len(results)} Retrieved Documents")
    #     print("=" * 70)

    #     for i, doc in enumerate(results, start=1):

    #         print(f"\nResult {i}")
    #         print("-" * 70)

    #         print(doc.page_content)

    #         print("\nMetadata")
    #         print(doc.metadata)

    #     print("\n")


if __name__ == "__main__":
    main()