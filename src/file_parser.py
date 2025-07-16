from data_loader import combined_doc
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma

def chunker(combined_document):
  splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
  chunked_docs= splitter.split_documents(combined_document)
  return chunked_docs

def vector_embedding(chunked_docs):
  model= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})

  vectordb= Chroma.from_documents(documents=chunked_docs, embedding=model, persist_directory=r'C:\Users\hyped\Desktop\RAG_Chatbot\db')

  return vectordb
