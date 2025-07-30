import pandas as pd #csv files
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.docstore.document import Document as LangDoc
import os
import tempfile
from docx import Document as docxLoader 

def read_pdf(file):
  with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
      temp_file.write(file.read()) 
      temp_path=temp_file.name  

  try:
          loader = PyMuPDFLoader(temp_path)
          documents = loader.load()
          cleaned_text = " ".join(doc.page_content.replace("-\n", "").replace("\n", " ") for doc in documents)

          return [LangDoc(page_content=cleaned_text, metadata={"source": file.name})]
  finally:
    os.remove(temp_path)

def read_docx_file(file):
  doc= docxLoader(file)
  text = "\n".join([p.text for p in doc.paragraphs])
  #print(text) : enable for testing
  return [LangDoc(page_content=text, metadata={"source":file.name})] 
  """ 
  => return [LangDoc(page_content=text)]
  this line convert the output extended into combined_docs from ['hello','hi','a','b','c','d'....] to this: ['hello','hi','abcd'...] 
  """

def read_txt(file):
  with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
      temp_file.write(file.read()) 
      temp_path = temp_file.name  

  try:
      with open(temp_path, 'r', encoding='utf-8') as f:
          content = f.read()
      return [LangDoc(page_content=content, metadata={"source": file.name})]
  finally:
      os.remove(temp_path)

def read_excel(file):
  doc=pd.read_excel(file)
  #print(doc) : enable for testing
  return doc

def read_csv(file):
  doc=pd.read_csv(file)
  #print(doc) : enable for testing
  return doc

def document_handler(uploaded_file):
  path_type= os.path.splitext(uploaded_file.name)[1].lower()
  print(path_type)
  
  #this modification to the loop below, adds the word and docx files into one document for chunking of data
  if path_type == ".pdf":
    return read_pdf(uploaded_file)
  elif path_type == ".docx":
    return read_docx_file(uploaded_file)
  elif path_type == ".xlsx":
    return read_excel(uploaded_file)
  elif path_type == ".csv":
    return read_csv(uploaded_file)
  elif path_type == ".txt":
    return read_txt(uploaded_file)

# TODO : Uncomment the return statement for further development of the model
# TODO : CSV & Excel sheet analysis