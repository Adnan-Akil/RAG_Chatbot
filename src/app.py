import streamlit as st
from data_loader import document_handler, combined_doc
from file_parser import chunker, vector_embedding
from retrieval import retrieve_similar_docs

st.title("Document Analysis Chatbot!")
uploaded_doc= st.file_uploader(label="Upload files for Analysis", accept_multiple_files=True)

if uploaded_doc:
  combined_doc.clear()
  for file in uploaded_doc:
    document_handler(file)
  
  if st.button("Process Documents"):
    chunks=chunker(combined_doc)
    vectordb=vector_embedding(chunks)
    st.success("Processed {len(chunks)} chunks into the vectordb")
  
user_query_text=st.text_input(label="Enter your Query:")
if user_query_text and st.button("Process the Query"):
  similar_results= retrieve_similar_docs(user_query_text)

  if similar_results:
    for i, doc in enumerate(similar_results, 1):
      st.markdown(f"**Result #{i}:**  {doc.page_content}")
  else:
    st.warning("No similar chunks found; try re-processing or refining your query.")

""" 
print(user_query_text)
print(chunker(combined_doc)) #: testing chunking
print(vector_embedding(chunker(combined_doc))) #: testing vector embedding 
"""