from langchain_core.prompts import PromptTemplate


RAG_PROMPT = PromptTemplate.from_template("""

    You are an intelligent HR assistant.

    Use only the provided context to answer the user's question.

    Do not use outside knowledge.

    If the answer cannot be found in the context,
    respond exactly:

    "I don't have enough information to answer that."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """)
   