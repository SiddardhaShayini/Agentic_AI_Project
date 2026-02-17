import chromadb
from sentence_transformers import SentenceTransformer
from load_pdf import load_pdf

# 1️⃣ Load PDF chunks
chunks = load_pdf("data\\my_document.pdf.pdf")

# 2️⃣ Initialize Chroma DB
client = chromadb.PersistentClient(path="embeddings/")
collection = client.create_collection(name="my_pdf_collection")

# 3️⃣ Initialize local embedding model (CPU-friendly)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 4️⃣ Add chunks to vector DB with embeddings
for i, chunk in enumerate(chunks):
    embedding_vector = model.encode(chunk).tolist()  # convert to list of floats
    collection.add(
        documents=[chunk],
        metadatas=[{"chunk": i}],
        ids=[str(i)],
        embeddings=[embedding_vector]
    )

print("Embedding creation complete! Total chunks:", len(chunks))
