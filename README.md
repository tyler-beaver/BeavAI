<div align="center">
  <h1>BeavAI: AI Research Copilot</h1>
	<img src="https://img.shields.io/badge/Python-3.14+-blue" />
  <img src="https://img.shields.io/badge/FastAPI-async-green" />
  <img src="https://img.shields.io/badge/Docker-ready-lightgrey" />
</div>

---

BeavAI is a production-ready agentic RAG (Retrieval-Augmented Generation) system for AI research, built with a modern stack for reliability and simplicity.

## Features
- Agent orchestration with LangGraph (LangChain ecosystem)
- Retrieval-Augmented Generation using FAISS
- REST API powered by FastAPI
- Persistent memory with SQLite
- Containerized deployment via Docker
- Easy integration with OpenAI GPT-5 (or Anthropic Claude)

## Tech Stack
| Component         | Technology           | Purpose                                      |
|-------------------|---------------------|-----------------------------------------------|
| Language          | Python 3.11+        | Standard for AI/ML, async support             |
| LLM API           | OpenAI GPT-3.5/4    | Reasoning, summarization, QA                  |
| Agent Framework   | LangGraph           | Multi-step reasoning, tool orchestration      |
| Vector DB         | FAISS (local)       | Fast vector search for RAG                    |
| Backend/API       | FastAPI             | Async REST API                                |
| Storage           | SQLite              | Persistent memory, conversation history        |
| Deployment        | Docker              | Consistent, reproducible environments         |
| Dev Tools         | VS Code, Git, venv  | Coding, version control, dependency isolation  |

## Quick Start
1. **Clone the repo:**
	```bash
	git clone <repo-url>
	cd BeavAI/ai-research-copilot
	```
2. **Install dependencies:**
	```bash
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	```
3. **Run the API server:**
   
	From the `ai-research-copilot` directory:
	```bash
	cd ai-research-copilot/app
	fastapi dev main.py
	```
	Or, using uvicorn (from the same directory):
	```bash
	uvicorn main:app --reload
	```
   
	If running from the project root, use:
	```bash
	fastapi dev ai-research-copilot/app/main.py
	# or
	uvicorn ai-research-copilot.app.main:app --reload
	```
4. **Test the API:**
	Visit [http://127.0.0.1:8000/ping](http://127.0.0.1:8000/ping) or use:
	```bash
	curl http://127.0.0.1:8000/ping
	```

## Project Structure
```
BeavAI/
  ai-research-copilot/
	 app/
		main.py
		agent/
		memory/
		services/
		tools/
	 data/
	 tests/
	 requirements.txt
	 Dockerfile
```
