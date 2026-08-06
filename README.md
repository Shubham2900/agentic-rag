# 🤖 Advanced RAG with LangGraph

> A progressive implementation of modern **Retrieval-Augmented Generation (RAG)** architectures using **LangGraph**, **LangChain**, **Ollama**, **ChromaDB**, and **Tavily Search**.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent_Workflows-00C853)
![LangChain](https://img.shields.io/badge/LangChain-LLM_Framework-2E7D32)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Database-purple)
![Tavily](https://img.shields.io/badge/Tavily-Web_Search-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

---

# 📖 Overview

This repository demonstrates the evolution of **Retrieval-Augmented Generation (RAG)** systems by progressively enhancing a traditional RAG pipeline into a production-style **Agentic AI** workflow.

Beginning with semantic retrieval, the project incrementally introduces document relevance grading, conditional web search, self-reflection, hallucination detection, answer validation, query rewriting, and adaptive routing using **LangGraph** state machines.

Rather than implementing separate applications, each stage builds upon the previous one to showcase how increasingly capable retrieval systems can be engineered.

---

# 🚀 Project Evolution

| Stage | Capability Introduced |
|--------|-----------------------|
| 📚 **Basic RAG** | Semantic retrieval using ChromaDB followed by grounded response generation. |
| 🤖 **Agentic RAG** | LLM-based document grading with conditional web search for missing knowledge. |
| 🔄 **Self-RAG** | Hallucination detection, answer grading, and query rewriting through self-reflection. |
| 🧠 **Adaptive RAG** | Intelligent query routing between vector retrieval and web search for improved efficiency. |

---

# 🏗 Evolution of the Workflow

```text
                 Basic RAG
                     │
                     ▼
               Agentic RAG
                     │
                     ▼
                 Self-RAG
                     │
                     ▼
               Adaptive RAG
```

---

# 🏛 Final Workflow

```text
                              User Question
                                    │
                                    ▼
                             Query Router
                                    │
                     ┌──────────────┴──────────────┐
                     ▼                             ▼
             Vector Retrieval                Web Search
                     │                             │
                     └──────────────┬──────────────┘
                                    ▼
                     Grade Retrieved Documents
                                    │
                     ┌──────────────┴──────────────┐
                     ▼                             ▼
             Generate Answer               Retrieve More
                     │
                     ▼
            Hallucination Detection
                     │
                     ▼
               Answer Evaluation
                     │
          ┌──────────┴───────────┐
          ▼                      ▼
     Return Answer         Rewrite Query
                                   │
                                   ▼
                            Retrieve Again
```

---

# ✨ Features

- 📚 Semantic Retrieval using ChromaDB
- 🤖 Agentic RAG Workflow
- 🔄 Self-RAG with Reflection
- 🧠 Adaptive Query Routing
- 🌐 Automatic Web Search using Tavily
- 📄 LLM-based Document Relevance Grading
- 🎯 Hallucination Detection
- ✅ Answer Quality Evaluation
- 🔁 Query Rewriting
- 📦 Structured Outputs using Pydantic
- 🔀 LangGraph State Machines
- ⚡ Local LLM Inference using Ollama
- 🧪 Unit Testing with Pytest

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Programming Language |
| 🔀 LangGraph | Agent Workflow Orchestration |
| 🦜 LangChain | LLM Framework |
| 🦙 Ollama | Local LLM Inference |
| 🧠 GPT-OSS 20B | Generation & Reasoning |
| 📚 ChromaDB | Vector Database |
| 🔎 Nomic Embed Text | Embedding Model |
| 🌐 Tavily Search | Web Search |
| 📄 Unstructured | Document Parsing |
| 🧪 Pytest | Testing Framework |

---

# 📂 Project Structure

```text
.
├── graph/
│   ├── chains/
│   │   └── tests/
│   ├── nodes/
│   ├── graph.py
│   ├── state.py
│   └── consts.py
│

├── ingestion.py
├── main.py
├── pyproject.toml
├── .env
└── README.md
```

---

# 🔄 Workflow Progression

## 📚 Basic RAG

```text
Question
    │
    ▼
Retrieve
    │
    ▼
Generate
```

---

## 🤖 Agentic RAG

```text
Question
      │
      ▼
Retrieve
      │
      ▼
Grade Documents
      │
 ┌────┴─────┐
 │          │
Generate   Web Search
      │      │
      └──┬───┘
         ▼
     Generate
```

---

## 🔄 Self-RAG

```text
Question
      │
      ▼
Retrieve
      │
      ▼
Generate
      │
      ▼
Hallucination Detection
      │
      ▼
Answer Grader
      │
 ┌────┴─────────┐
 │              │
Accept     Rewrite Query
                 │
                 ▼
            Retrieve Again
```

---

## 🧠 Adaptive RAG

```text
Question
      │
      ▼
Query Router
      │
 ┌────┴────────┐
 │             │
Vector     Web Search
Search
 │             │
 └────┬────────┘
      ▼
 Retrieve
      │
      ▼
Grade Documents
      │
      ▼
Generate
```

---

# ⚙ Installation

Clone the repository.

```bash
git clone https://github.com/Shubham2900/agentic-rag.git

cd agentic-rag
```

Create a virtual environment.

```bash
uv venv
```

Install dependencies.

```bash
uv sync
```

---

# 🤖 Ollama Setup

Pull the required models.

```bash
ollama pull gpt-oss:20b

ollama pull nomic-embed-text
```

Start the Ollama server.

```bash
ollama serve
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
TAVILY_API_KEY=your_api_key
```

---

# 📚 Build the Vector Store

Run the ingestion pipeline to download, split, embed, and index the knowledge base.

```bash
python ingestion.py
```

The vector database will be stored locally inside:

```text
.chroma/
```

---

# ▶ Running the Project

```bash
python main.py
```

Example Output

```text
Hello Advanced RAG

Retrieving Documents...

Grading Retrieved Documents...

Performing Web Search (if required)...

Checking Hallucinations...

Evaluating Answer...

Done ✅
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 📖 Knowledge Sources

The vector database is created from the following technical articles by **Lilian Weng**:

- 🤖 LLM Powered Autonomous Agents
- ✍️ Prompt Engineering
- 🛡️ Adversarial Attacks on Large Language Models

---

# 🎯 Learning Outcomes

This repository demonstrates practical implementations of:

- Retrieval-Augmented Generation (RAG)
- Agentic AI Workflows
- LangGraph State Machines
- Semantic Search
- Vector Databases
- Reflection-based Reasoning
- Hallucination Detection
- Adaptive Retrieval
- Query Routing
- Query Rewriting
- Local LLM Deployment
- Structured LLM Outputs
- Context-Aware Response Generation

---

# 🚀 Roadmap

- ✅ Basic RAG
- ✅ Agentic RAG
- ✅ Self-RAG
- ✅ Adaptive RAG
- ⏳ Corrective RAG (CRAG)
- ⏳ Graph RAG
- ⏳ Hybrid Search (BM25 + Vector Search)
- ⏳ Multi-Agent RAG
- ⏳ MCP Integration
- ⏳ Long-Term Memory
- ⏳ Evaluation Framework
- ⏳ Streaming Responses

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve an existing workflow or implement another advanced RAG architecture, feel free to open an issue or submit a pull request.

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork it
- 🛠️ Contribute improvements
- 📢 Share it with the AI community

---

<div align="center">

### 🚀 Building Production-Ready Agentic RAG Systems with LangGraph

**Made with ❤️ using Python, LangGraph, LangChain, Ollama, ChromaDB & Tavily Search**

</div>