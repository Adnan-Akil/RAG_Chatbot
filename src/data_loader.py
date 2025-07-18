import pandas as pd #csv files
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.docstore.document import Document as LangDoc
from unstructured.partition.auto import partition
import os
import tempfile #for pdfLoading
from docx import Document as docxLoader #for docx loading
combined_doc=[]

def read_pdf(file):
  with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
      temp_file.write(file.read()) 
      temp_path=temp_file.name  #this creates a temp path and stores the file there for being read by the pymupdf

  try:
    elements = partition(filename=temp_path)
    full_text = "\n\n".join(str(elem.text) for elem in elements if hasattr(elem, "text")) #this does partitioning based on layout

    cleaned = full_text.replace("-\n", " ")
    cleaned = " ".join(cleaned.split()) #this step cleans all the hyphens and unwanted spaces

    return [LangDoc(page_content=cleaned, metadata={"source": file.name})]
  
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
    combined_doc.extend(read_pdf(uploaded_file))
  elif path_type == ".docx":
    combined_doc.extend(read_docx_file(uploaded_file))
  if path_type == ".xlsx":
    doc= read_excel(uploaded_file)
  elif path_type == ".csv":
    doc= read_csv(uploaded_file)

# TODO : Uncomment the return statement for further development of the model
# TODO : CSV & Excel sheet analysis