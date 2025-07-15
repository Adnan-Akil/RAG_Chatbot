import streamlit as st
from data_loader import doc_handler, combined_doc
from file_parser import chunker, vector_embedding

st.title("Document Analysis Chatbot!")

uploaded_doc= st.file_uploader(label="Upload files for Analysis", accept_multiple_files=True)
for file in uploaded_doc:
  doc_handler(file)
  
""" 
enable for testing: 
print(chunker(combined_doc)) : testing chunking
print(vector_embedding(chunker(combined_doc))) : testing vector embedding 
"""