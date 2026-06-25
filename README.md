# 🤖 LangGraph + PostgreSQL AI Chatbot

A LangGraph-powered conversational AI chatbot built using **FastAPI**, **LangChain**, **Groq LLM**, and **PostgreSQL persistent memory**.

This project demonstrates how to build an AI chatbot with graph-based workflows and store conversation states using PostgreSQL as a LangGraph checkpointer.

---

# 🚀 Features

- ✅ LangGraph workflow-based chatbot
- ✅ PostgreSQL persistent conversation memory
- ✅ FastAPI backend API
- ✅ Groq LLM integration
- ✅ Conversation state management
- ✅ Automatic conversation summarization
- ✅ Environment variable configuration
- ✅ Custom logging system
- ✅ Swagger API documentation
- ✅ Docker support

---

# 🏗️ Architecture

```
                 User
                   |
                   |
            FastAPI Endpoint
              (/chat API)
                   |
                   |
            LangGraph Workflow
                   |
        -------------------------
        |                       |
   Chatbot Node            Summary Node
        |
        |
      Groq LLM
        |
        |
 PostgreSQL Checkpointer
        |
        |
 Conversation Memory
```

---

# 🛠️ Tech Stack

## Backend
- Python
- FastAPI

## AI Framework
- LangGraph
- LangChain

## LLM
- Groq API
- ChatGroq

## Database
- PostgreSQL
- Supabase

## Testing
- Swagger UI

## Deployment
- Docker

---

# 📂 Project Structure

```
langgraph-postgres/

│
├── config/
│   ├── __init__.py
│   └── settings.py
│       # Environment configuration
│       # Database URL
│       # Model settings
│
├── database/
│   └── tables.py
│       # PostgreSQL table initialization
│
├── exception/
│   ├── __init__.py
│   └── errors.py
│       # Custom exception handling
│
├── logger/
│   ├── __init__.py
│   └── customlogger.py
│       # Application logger
│
├── prompt/
│   ├── chatbot_prompt.py
│   └── summary_prompt.py
│       # LLM prompt templates
│
├── src/
│   │
│   ├── main.py
│   │   # FastAPI application
│   │
│   ├── graph.py
│   │   # LangGraph workflow
│   │   # PostgreSQL checkpointer
│   │
│   ├── chatbot.py
│   │   # Chatbot processing node
│   │
│   ├── summary.py
│   │   # Summary generation node
│   │
│   └── models/
│       ├── schemas.py
│       │   # API request and response models
│       │
│       └── state.py
│           # LangGraph state definition
│
├── utils/
│   ├── __init__.py
│   └── llm.py
│       # Groq LLM initialization
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone <repository-url>

cd langgraph-postgres
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=your_groq_api_key

POSTGRES_URL=your_postgresql_connection_string
```

---

# 🗄️ Database Setup

Initialize LangGraph PostgreSQL tables:

```bash
python database/tables.py
```

This creates required LangGraph tables:

```
checkpoints
checkpoint_blobs
checkpoint_writes
```

These tables store chatbot conversation states.

---

# ▶️ Run Application

Start FastAPI server:

```bash
uvicorn src.main:app --reload
```

Server will run:

```
http://127.0.0.1:8000
```

---

# 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```



# 🐳 Docker Usage

Build Docker image:

```bash
docker build -t langgraph-chatbot .
```

Run container:

```bash
docker run -p 8000:8000 langgraph-chatbot
```

---

# 🔍 Database Verification

Open PostgreSQL/Supabase SQL Editor:

```sql
SELECT * FROM checkpoints;
```

Conversation checkpoints can be viewed here.

---
