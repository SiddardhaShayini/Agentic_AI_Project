import PyPDF2
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(file_path, chunk_size=500, chunk_overlap=50):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_text(text)
    return chunks

if __name__ == "__main__":
    chunks = load_pdf("data\\my_document.pdf.pdf")
    print(f"Total chunks: {len(chunks)}")
    print("Sample chunk:\n", chunks[0])
