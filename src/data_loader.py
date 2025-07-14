import pandas as pd #csv files
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
import os
import tempfile
from docx import Document

def read_pdf(file):
  with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
      temp_file.write(file.read()) 
      temp_path=temp_file.name  #this creates a temp path and stores the file there for being read by the pymupdf

  loader= PyMuPDFLoader(temp_path) #pymupdf doesnt accept an uploaded file, it reads files from the Path
  doc=loader.load()
  #print(doc) #enable for testing
  os.remove(temp_path)
  return doc

def read_docx_file(file):
  doc= Document(file)
  text = "\n".join([p.text for p in doc.paragraphs])
  #print(text) #enable for testing
  return text

def doc_handler(uploaded_file):
  path_type= os.path.splitext(uploaded_file.name)[1].lower()
  print(path_type)

  if path_type == ".pdf":
    doc= read_pdf(uploaded_file)
  elif path_type == ".docx":
    doc= read_docx_file(uploaded_file)
    
doc_handler