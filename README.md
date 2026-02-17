# Personal Research Assistant – Offline Agentic AI

An **offline, multi-step agentic AI** Personal Research Assistant that uses **RAG (Retrieval-Augmented Generation)** with **local embeddings**, **ChromaDB**, and **Ollama Phi-3** to read, summarize, and provide actionable insights from PDFs. It demonstrates **MCP/A2A multi-step reasoning**, fully offline and CPU-friendly.

---

## Features

* Fully **offline**: no APIs required, all embeddings and models run locally.
* **PDF ingestion**: load and chunk any PDF for analysis.
* **Local embeddings**: CPU-friendly `SentenceTransformers` embeddings (`all-MiniLM-L6-v2`).
* **Vector DB**: stores PDF chunks using **ChromaDB** (persistent storage).
* **RAG-based retrieval**: fetches relevant context based on user query.
* **Agentic AI reasoning**: multi-step reasoning (MCP/A2A) using Ollama Phi-3.
* **Interactive CLI**: ask questions, get structured multi-step outputs.
* **Extensible**: can handle multiple PDFs and expand reasoning steps.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SiddardhaShayini/Agentic_AI_Project.git
```
```bash
cd personal_research_assistant
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install Ollama and download model:

```bash
ollama list          # Check installed models
```
```bash
ollama pull phi-3    # Download Phi-3 locally
```
> Optional: use `phi-1` or `phi-2` for faster CPU testing.

---

## Usage

### **Step 1 – Load and Chunk PDF**

```bash
python scripts/load_pdf.py
```

* Outputs total chunks and a sample chunk.
* Chunks are saved in memory for embeddings.

---

### **Step 2 – Create Embeddings**

```bash
python scripts/create_embeddings.py
```

* Uses **`SentenceTransformer`** to create embeddings for PDF chunks.
* Stores embeddings persistently in `embeddings/` folder.
* Works **offline and CPU-friendly**.

---

### **Step 3 – Query via RAG (Optional Test)**

```bash
python scripts/rag_query.py
```

* Queries the vector DB using a sample question.
* Retrieves top-k relevant chunks and generates LLM answer.
* Example:

```
Question: Explain the main idea of the PDF
Answer: Strategic Adaptations in Financial Systems and Economic Policies for Sustainable Development Amidst Technological Transformation
```

---

### **Step 4 – Full Agentic AI Interaction**

Run CLI:

```bash
python main.py
```

* Enter any question about the loaded PDF.
* Example input: `summarize the document`
* Example output:

```
Step 1 Result:
The article discusses strategies for improving sustainability in winemaking through text mining-based comparative analysis of voluntary national reviews from various countries...

Step 2 Result:
The article presents an analysis comparing voluntary national reviews related to environmental practices in winemaking using text mining techniques...

Step 3 Result:
Explore renewable energy sources such as solar power systems, wind plants, sustainable agriculture, and community awareness programs for environmental sustainability.
```

---

## Architecture

1. **PDF Loader (`load_pdf.py`)**

   * Loads PDF and splits text into chunks (~500 tokens per chunk).

2. **Local Embeddings (`create_embeddings.py`)**

   * Uses `SentenceTransformers` to generate embeddings for each chunk.
   * Stores embeddings in **persistent ChromaDB** for offline use.

3. **RAG Query (`rag_query.py`)**

   * Retrieves top-k relevant chunks from ChromaDB for a question.
   * Generates LLM response with **Ollama Phi-3**.

4. **Agentic AI (`agentic_ai.py`)**

   * Multi-step reasoning pipeline (MCP/A2A):

     * Step 1: Extract key points
     * Step 2: Summarize cohesively
     * Step 3: Suggest actionable next steps

5. **CLI (`main.py`)**

   * Interactive prompt to enter questions.
   * Returns multi-step outputs for reasoning and action planning.

---

## Example Results

**Question:** `summarize the document`

**Step 1 Output:**

* Extracted strategies in environmental sustainability and financial policies from multiple research papers.

**Step 2 Output:**

* Summarized findings into cohesive insights about sustainable development and policy formulation.

**Step 3 Output:**

* Suggested actionable directions: renewable energy adoption, sustainable agriculture, community education programs.

> Demonstrates **MCP/A2A multi-step reasoning** with **offline RAG context retrieval**.

---

## Notes

* Fully **offline**, no API keys required.
* CPU-friendly, works on laptops without GPU.
* Supports **multi-step agentic reasoning** using Ollama local LLM.
* Persistent vector DB ensures repeated queries are fast and efficient.
* Can scale to multiple PDFs or research documents by adding them to `data/`.

---

## Future Enhancements

* Add **dynamic step reasoning** for unlimited MCP/A2A steps.
* Expand UI with **Streamlit** or **Gradio** interface.
* Add **multi-document RAG search** for larger research corpora.
* Include **session memory** to remember prior user queries.

---

## References

* [ChromaDB](https://www.trychroma.com/) – open-source vector DB
* [SentenceTransformers](https://www.sbert.net/) – local embeddings
* [LangChain Ollama](https://python.langchain.com/en/latest/modules/models/llms/integrations/ollama.html) – LLM integration
* Ollama Phi-3 model – local LLM

---

## 👨‍💻 Developer
**Siddardha Shayini**  
