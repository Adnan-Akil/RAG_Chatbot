import streamlit as st
from data_loader import document_handler
from file_parser import build_index, vector_store, clear_vector_store
from retrieval import retrieve_similar_docs
from llm import final_answer

st.title("Document Analysis Chatbot!", width="stretch")
uploaded_doc= st.file_uploader(label="Upload files for Analysis", accept_multiple_files=True)

if uploaded_doc:
  if st.button("Process Documents"):
    clear_vector_store(vector_store)
    for file in uploaded_doc:
      processed_doc= document_handler(file)
      build_index(processed_doc)
  
    st.success("Processed and Indexed the Data!")
    
user_query_text=st.text_input(label="Enter your Query:")
if user_query_text and st.button("Process the Query"):

  similar_results= retrieve_similar_docs(user_query_text)  
  print(similar_results)
  
  if similar_results:
    st.write(final_answer(similar_results,user_query_text))
  else:
    st.warning("No similar chunks found; try re-processing or refining your query.")
