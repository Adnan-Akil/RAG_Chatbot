import pandas as pd #csv files
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
import os
import tempfile #for pdfLoading
from docx import Document #for docx loading

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

def read_excel(file):
  doc=pd.read_excel(file)
  #print(doc)
  return doc

def read_csv(file):
  doc=pd.read_csv(file)
  #print(doc)
  return doc

def doc_handler(uploaded_file):
  path_type= os.path.splitext(uploaded_file.name)[1].lower()
  print(path_type)

  if path_type == ".pdf":
    doc= read_pdf(uploaded_file)
  elif path_type == ".docx":
    doc= read_docx_file(uploaded_file)
  elif path_type == ".xlsx":
    doc= read_excel(uploaded_file)
  elif path_type == ".csv":
    doc= read_csv(uploaded_file)
    
doc_handler