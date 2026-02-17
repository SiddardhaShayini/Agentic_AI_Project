from rag_query import query_rag

def agentic_task(question):
    # Multi-step plan example (MCP)
    plan = [
        "Step 1: Retrieve relevant information",
        "Step 2: Summarize the content",
        "Step 3: Suggest next action"
    ]
    results = []
    for step in plan:
        if "Retrieve" in step:
            results.append(query_rag(question))
        elif "Summarize" in step:
            summary = query_rag(f"Summarize this: {results[-1]}")
            results.append(summary)
        elif "Suggest" in step:
            suggestion = query_rag(f"Based on above, suggest next step to learn more")
            results.append(suggestion)

    return results

if __name__ == "__main__":
    question = "Explain the main points of the PDF"
    outputs = agentic_task(question)
    for i, out in enumerate(outputs):
        print(f"Step {i+1} Output:\n{out}\n{'-'*50}")
