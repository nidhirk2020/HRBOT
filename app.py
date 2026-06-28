from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq

from config import embedding_model, GROQ_API_KEY


loader = PyPDFDirectoryLoader("Data") 
# data folder has pdfs
documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

# print("Total Chunks:", len(chunks))

# print(chunks[0].page_content)

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)
# print("Vector Database Created Successfully!")

# Load Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0
)


while True:

    query = input("\nAsk your question to HRBOT (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    docs = vector_db.similarity_search(query, k=3)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an HR assistant.

Answer ONLY from the provided context.

If the answer isn't available, reply:
"I couldn't find this information in the HR documents."

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:\n")
    print(response.content)