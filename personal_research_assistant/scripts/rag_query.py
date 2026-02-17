import chromadb
from langchain_ollama import OllamaLLM

# Persistent client
client = chromadb.PersistentClient(path="embeddings/")  # persistent DB

# Ensure collection exists
if "my_pdf_collection" in [c.name for c in client.list_collections()]:
    collection = client.get_collection("my_pdf_collection")
else:
    raise ValueError("Collection 'my_pdf_collection' does not exist. Run create_embeddings.py first!")

# Initialize LLM
llm = OllamaLLM(model="phi3")  # Ollama Phi-3 local

def query_rag(question, top_k=3):
    results = collection.query(
        query_texts=[question],
        n_results=top_k
    )
    retrieved_docs = [r for r in results['documents'][0]]
    context = "\n".join(retrieved_docs)

    prompt = f"Answer the following question using the context below:\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"

    # Use .generate() instead of calling llm
    llm_response = llm.generate([prompt])
    answer = llm_response.generations[0][0].text
    return answer

if __name__ == "__main__":
    q = "Explain the main idea of the PDF"
    ans = query_rag(q)
    print("Answer:\n", ans)
