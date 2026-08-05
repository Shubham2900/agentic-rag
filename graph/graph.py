from dotenv import load_dotenv
from langgraph.graph import END, StateGraph
from graph.consts import RETRIEVE, GENERATE, GRADE_DOCUMENTS, WEBSEARCH
from graph.nodes.retrieve import retrieve
from graph.nodes.generate import generate
from graph.nodes.grade_documents import grade_documents
from graph.nodes.web_search import web_search
from graph.state import GraphState

load_dotenv()

def decide_to_generate(state):
    print("---Assess Graded Documents---")
    if state["web_search"]:
        print("---Decision: Not all Documents Relevant to question")
        return WEBSEARCH
    else:
        print("---Decision: Generate")
        return GENERATE

workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(WEBSEARCH, web_search)
workflow.add_node(GENERATE, generate)

workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    }
)
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()
