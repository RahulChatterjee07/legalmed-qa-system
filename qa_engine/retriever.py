# retriever.py

def simple_retrieval(question, knowledge_base):
    """
    Given a question and a simulated knowledge base (list of dict),
    return the most relevant context.
    """
    for doc in knowledge_base:
        if any(keyword.lower() in doc['content'].lower() for keyword in question.split()):
            return doc['content'], doc['source']
    return "Not found", "N/A"


if __name__ == "__main__":
    # Simulated knowledge base
    kb = [
        {"content": "The last assessment was performed on March 12, 2024.", "source": "Form A, Page 2"},
        {"content": "Claimant completed rehabilitation on February 1, 2023.", "source": "Rehab Report"}
    ]

    q = "When was the last assessment?"
    context, source = simple_retrieval(q, kb)
    print("🔍 Retrieved Context:", context)
    print("📄 Source:", source)
