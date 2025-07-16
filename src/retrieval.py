from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def retrieve_similar_docs(user_query_text):
  #embedding the user query
  model= HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={"device": "cpu"})
  embedded_user_query = model.embed_query(user_query_text)

  #load the existing vectorDB
  vectordb=Chroma(persist_directory=r"C:\Users\hyped\Desktop\RAG_Chatbot\db", embedding_function=model)
  #retieval of similar chunks
  retrieved_docs=vectordb.similarity_search_by_vector(embedded_user_query,k=5)

  return retrieved_docs
