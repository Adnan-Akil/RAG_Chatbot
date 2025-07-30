import streamlit as st
from data_loader import document_handler
from file_parser import build_index, vector_store, clear_vector_store
from retrieval import retrieve_similar_docs
from llm import final_answer

# ✅ Streamlit configuration
st.set_page_config(page_title="Data Chat📚", layout="wide")
st.markdown(
  "<h1 style='text-align: center; font-size: 3em; font-family: Times New Roman, Times, serif; font-weight: bold;'>Q&amp;A with Your Documents 📖</h1>",
  unsafe_allow_html=True
)

# Sidebar: document upload & processing
with st.sidebar:
    st.header("Document Management")
    uploaded_docs = st.file_uploader(
        label="Upload your documents",
        accept_multiple_files=True
    )
    if st.button("Process Documents"):
        if not uploaded_docs:
            st.warning("Please upload one or more files first.")
        else:
            with st.spinner("Processing documents..."):
                clear_vector_store(vector_store)
                for file in uploaded_docs:
                    processed = document_handler(file)
                    build_index(processed)
                st.success("Documents processed and indexed!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Upload documents to begin chatting."}
    ]

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input and response
if prompt := st.chat_input("Ask about your documents..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("assistant"):
    with st.spinner("Thinking..."):
      similar_chunks = retrieve_similar_docs(prompt)
      if similar_chunks:
        answer = final_answer(similar_chunks, prompt)
        st.write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
      else:
        st.warning("No similar chunks found; try re-uploading or refining your query.")
