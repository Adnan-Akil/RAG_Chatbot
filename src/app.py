import streamlit as st
from data_loader import doc_handler, combined_doc
from file_parser import chunker

st.title("Document Analysis Chatbot!")

uploaded_doc= st.file_uploader(label="Upload files for Analysis", accept_multiple_files=True)
for file in uploaded_doc:
  doc_handler(file)
  
print(chunker(combined_doc))