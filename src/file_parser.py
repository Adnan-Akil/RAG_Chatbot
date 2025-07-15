from data_loader import combined_doc
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunker(combined_document):
  splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
  chunked_docs= splitter.split_documents(combined_document)
  
  """ print(f"Total chunks: {len(chunked_docs)}")
  for i, chunk in enumerate(chunked_docs[:]):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk.page_content[:]) 
  """ #enable for testing
  return chunked_docs
