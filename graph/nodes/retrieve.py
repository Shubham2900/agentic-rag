from typing import Any, Dict 
from graph.state import GraphState
from ingestion import retriever

def retrieve(state: GraphState) -> Dict[str, Any]:
    print(f"Retrieving documents for question: {state['question']}")
    query = state['question']
    docs = retriever.invoke(query)
    return {
        "documents": docs,
        "question": query,
    }