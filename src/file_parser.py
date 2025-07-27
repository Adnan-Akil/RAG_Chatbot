from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma.vectorstores import Chroma

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200, chunk_overlap=400
)

vector_store=Chroma(
        embedding_function=embedding_model,
        persist_directory=r"C:\Users\hyped\Desktop\RAG_Chatbot\db"
    )

def build_index(combined_doc):
    chunks = splitter.split_documents(combined_doc)
    vector_store.add_documents(chunks)
    print(f"Indexed {len(chunks)} chunks into Storage")

def clear_vector_store(store):
    all_ids = store.get()["ids"]
    if all_ids:
        store.delete(ids=all_ids)
        print(f"Deleted {len(all_ids)} documents from the vector store.")
    else:
        print("No documents to delete.")
