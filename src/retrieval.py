from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

def retrieve_similar_docs(user_query_text):
  #embedding the user query
  model= HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={"device": "cpu"})
  embedded_user_query = model.embed_query(user_query_text)

  #load the existing vectorDB
  vectordb=Chroma(embedding_function=model)
  #persist_directory=r"C:\Users\hyped\Desktop\RAG_Chatbot\db",
  #retrieval + re-ranking!!
  base_retriever=vectordb.as_retriever(search_kwargs={"k":10})
  encoder_model=HuggingFaceCrossEncoder(model_name='cross-encoder/ms-marco-MiniLM-L-6-v2', model_kwargs={"device": "cpu"})
  reranker=CrossEncoderReranker(model=encoder_model, top_n=5)
  final_retriever=ContextualCompressionRetriever(base_retriever=base_retriever, base_compressor=reranker)

  return final_retriever.get_relevant_documents(user_query_text)
