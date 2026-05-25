# 🤖 Modular Local RAG System

A fully local Retrieval-Augmented Generation (RAG) chatbot built using FAISS, Sentence Transformers, TinyLlama, Ollama, and Streamlit.

---

## 🚀 Features

- 📄 PDF ingestion pipeline
- ✂️ Intelligent text chunking
- 🧠 Semantic embeddings using Sentence Transformers
- 🔍 Fast vector retrieval with FAISS
- 🤖 Local LLM responses using TinyLlama + Ollama
- 🌐 Streamlit web interface
- 🧩 Modular backend architecture
- 🔒 Fully offline/local AI workflow

---

## 🏗️ Architecture

```text
PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS Vector Store
 ↓
Retriever
 ↓
TinyLlama (Ollama)
 ↓
AI Response
```

---

## 📂 Project Structure

```text
modular-local-rag-system/
│
├── app.py
├── ask.py
├── ingest.py
├── modules/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── generator.py
│
├── data/
├── assets/
├── requirements.txt
└── README.md
```

---

## 🖼️ Demo Screenshots

### Home Interface

![Homepage](assets/homepage.png)

---

### AI Answer Generation

![Answer Demo](assets/answer-demo.png)

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/vansh-13042005/modular-local-rag-system.git
cd modular-local-rag-system
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
.\venv\Scripts\Activate.ps1
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install and Run Ollama

Install Ollama:

https://ollama.com

Run TinyLlama:

```bash
ollama run tinyllama
```

---

### 5. Launch Application

```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Ollama
- TinyLlama
- PyTorch

---

## 🔮 Future Improvements

- Multi-PDF support
- Chat history memory
- Better local models (Mistral/Phi-3)
- Source citations
- Docker deployment
- FastAPI backend
- React frontend

---

## 👨‍💻 Author

Vansh Tomar
