RAG_Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with Python and Streamlit, integrating LangChain, HuggingFace embeddings, and a local vector database (ChromaDB) to deliver precise and context-aware responses from custom documents such as contracts, policies, or any text corpus.

📌 Table of Contents
Project Overview

Key Features

Architecture & Pipeline

Getting Started

Prerequisites
Installation
Usage

Future Enhancements

Contributing

📝 Project Overview
This RAG_Chatbot leverages the power of large language models (LLMs) combined with a vector retrieval database to answer user queries based on custom document collections. Users can upload PDFs, Word documents, or text files; the system will:

Chunk & Embed: Break documents into semantic chunks and generate embeddings.
Store: Save embeddings in ChromaDB for fast similarity search.
Retrieve & Rerank: On user query, retrieve top-N relevant chunks via MMR, then rerank using CrossEncoder for precision.
Generate: Compose a final, coherent answer by prompting the LLM with retrieved contexts.
Streamlit UI: Interactive frontend allowing uploads, chat interface, and session state.
✨ Key Features
Streamlit-based UI: Simple, responsive chat interface.
Document Ingestion: Support for PDF, TXT, and DOCX.
Chunking Module: Customizable chunk size & overlap.
Embeddings: HuggingFace sentence-transformers.
Vector Store: ChromaDB with optional persistence.
Retrieval: Maximum Marginal Relevance (MMR) + CrossEncoder re-ranking.
Error Handling: Robust logging, hides stack traces from end-users.
🏗 Architecture & Pipeline

🚀 Getting Started
Prerequisites
Python 3.9+
pip or poetry
Git
Installation
Clone the repository:

git clone https://github.com/Adnan-Akil/RAG_Chatbot.git
cd RAG_Chatbot
Create & activate virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\\Scripts\\activate  # Windows
Install dependencies:

pip install -r requirements.txt
Setup the API key from GROQ website using any model of choice

💬 Usage
Launch the Streamlit app:

streamlit run src/app.py
Navigate to http://localhost:8501
Upload documents and start chatting!
🔮 Future Enhancements
Extensive Data Analysis Module:

CSV & Excel Support: Ingest large numeric datasets via pandas. Numeric Analytics: Compute statistics, trends, correlations, and aggregations. Visualization: Integrate matplotlib or plotly for charts (line, bar, scatter). Streamlit Components: Tabs for Data Overview, Summary Statistics, Plots, and Download Reports.

Enhanced UI/UX:

Dark/light mode toggle.
Custom CSS for branding.
Memory & Context Window:

Store conversation history in vectorDB for long-term context.
Authentication & Security:

User login & permission control.
Multi-Language Support:

Extend to other languages via multilingual embeddings.
🤝 Contributing
Contributions welcome! Please follow the standard GitHub flow:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add feature')
Push to the branch (git push origin feature/your-feature)
Open a Pull Request
> Built with ❤️ by Adnan Akil.