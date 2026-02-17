import sys
sys.path.append("scripts")
from agentic_ai import agentic_task

if __name__ == "__main__":
    print("Welcome to Personal Research Assistant!\n")
    question = input("Enter your question: ")
    outputs = agentic_task(question)
    for i, out in enumerate(outputs):
        print(f"\nStep {i+1} Result:\n{out}\n")
