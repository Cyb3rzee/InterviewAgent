# InterviewAgent — Local-First Grounded AI Interview Agent

InterviewAgent is an open-source, local-first RAG (Retrieval-Augmented Generation) agent engineered to conduct mock interviews and generate candidate responses strictly anchored to a deterministic JSON knowledge base.

## Architecture Overview

- **Engine:** Local LLM via Ollama (`llama3.2:3b`)
- **Retrieval Layer:** Weighted relevance-scoring retriever (`memory/retrieval.py`)
- **UI:** Streamlit dashboard with real-time token streaming (`app.py`)
- **Security Control:** Hallucination mitigation via system prompt constraints and context isolation

## Directory Structure

```text
InterviewAgent/
├── agent/
│   ├── orchestrator.py      # LLM connection & token streaming logic
│   └── question_analyzer.py # Intent parsing
├── candidate/
│   └── profile.json         # Candidate ground-truth database
├── memory/
│   └── retrieval.py         # Context matching engine
├── app.py                   # Streamlit interface
├── requirements.txt         # Project dependencies
└── README.md