
# AI Support Copilot with RAG and Tool Calling

AI Support Copilot is a business-oriented AI assistant designed to help customer support teams analyze incoming support tickets, retrieve relevant knowledge base information, interact with internal APIs, and generate structured support responses.

The system is built with **Python, FastAPI, LangGraph, LangChain, and Ollama**, and demonstrates how modern **LLM-based agent systems** can integrate with business workflows.

The application exposes its functionality through a **FastAPI backend with Swagger documentation** and includes a **minimal web interface** for interactive testing.

---

# Features

- Support ticket analysis
- Ticket classification and prioritization
- Retrieval-Augmented Generation (RAG) over internal support documentation
- Tool calling with internal business APIs
- Suggested customer support replies
- FastAPI backend with Swagger / OpenAPI documentation
- Minimal front-end for interactive testing
- Local LLM inference with Ollama
- Modular architecture for agent workflows

---

# Business Scenario

This project simulates an **AI copilot used by a SaaS customer support team**.

The assistant helps support agents handle customer issues faster and more consistently by:

- analyzing support tickets
- retrieving relevant company policies
- calling internal APIs when needed
- generating support-ready replies

Example issues the system can handle:

- login problems
- billing issues
- refund requests
- subscription cancellation
- incident-related customer questions
- policy-based support responses

---

# Example Workflow

1. A customer support ticket is submitted
2. The AI agent analyzes the issue
3. Relevant knowledge base documents are retrieved
4. Internal business APIs are queried if necessary
5. The system generates a suggested response
6. The response is returned through the API or UI

---

# System Architecture

User / Support Agent
    |
    v
Minimal Web UI
    |
    v
FastAPI Backend
    |
    v
LangGraph Agent Workflow
   /     |      \
  /      |       \
LLM     RAG     Tool Calls
(Ollama)          |
             Internal APIs

---

# Tech Stack

Core Technologies
- Python
- FastAPI
- LangGraph
- LangChain
- Ollama

Data and Retrieval
- Vector Database (ChromaDB or FAISS)
- Markdown Knowledge Base
- Support Ticket Dataset

Frontend
- HTML
- CSS
- JavaScript

Infrastructure
- Swagger / OpenAPI
- Docker (optional)

---

# Dataset

Customer Support Tickets Dataset (200k records)

https://www.kaggle.com/datasets/mirzayasirabdullah07/customer-support-tickets-dataset-200k-records

The dataset is used to simulate realistic support scenarios such as:

- ticket classification
- support workflows
- response generation
- analysis of customer issues

---

# Knowledge Base

The system includes a simulated internal support knowledge base with documents such as:

- refund policy
- account recovery guide
- billing troubleshooting
- subscription cancellation procedures
- API authentication errors
- incident response playbook

These documents are indexed into a **vector database** and used for **Retrieval-Augmented Generation (RAG)**.

---

# Internal Business APIs

Example APIs available to the AI agent:

GET /api/v1/customers/{customer_id}
GET /api/v1/subscriptions/{subscription_id}
POST /api/v1/refunds/check-eligibility
GET /api/v1/incidents/active

These simulate internal enterprise systems such as CRM, billing services, and incident management platforms.

---

# Project Structure

ai-support-copilot-rag/

app/
  api/        # FastAPI routes
  agents/     # LangGraph workflows
  services/   # LLM + RAG logic
  tools/      # API tools used by the agent
  models/     # Pydantic schemas
  core/       # configuration and logging

data/
  raw/
  processed/
  mock/

knowledge_base/
frontend/
scripts/
tests/

---

# API Documentation

Swagger UI will be available at:

/docs

Example endpoints:

POST /api/v1/tickets/analyze
POST /api/v1/chat
GET /api/v1/customers/{customer_id}
GET /api/v1/subscriptions/{subscription_id}
POST /api/v1/refunds/check-eligibility
GET /api/v1/incidents/active
GET /health

---

# Local Development

Clone the repository

git clone <your-repository-url>
cd ai-support-copilot-rag

Create virtual environment

python -m venv .venv
source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

---

# Run Ollama

Example:

ollama pull llama3

---

# Run the application

uvicorn app.main:app --reload

API:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs

---

# Future Improvements

- human-in-the-loop approval
- multi-agent workflows
- ticket similarity search
- escalation recommendations
- observability and tracing
- authentication and role-based access
- production deployment with Docker

---

# Project Goals

Demonstrate how to build **enterprise AI systems** combining:

- LLMs
- Retrieval-Augmented Generation
- Agent workflows
- Business API integrations

---

# Author

AI / Data Engineering Portfolio Project
