from langchain_ollama.llms import OllamaLLM

def final_answer(retrieved_docs, user_query):
  llm_model= OllamaLLM(model='llama3.2',temperature=0.1)

  template = f"""
  You are a helpful, precise assistant.
  Your task is to provide an answer to the user using ONLY the following context. Do not use any external knowledge or guess.

  Context:
  {retrieved_docs}

  User question:
  {user_query}

  Instructions:
  - Only answer using the context above.
  - If the context does not contain enough information, reply: "I’m sorry, but the context does not provide enough information to answer this question."
  - Write clearly and concisely.
  - Use bullet points or headings IF it improves clarity.
  - Do not add anything extra.
  - Use proper formatting for the answers, headings in one line, bullet points each in a new line etc.

  Answer:
  """

  llm_response = llm_model.invoke(template)
  return llm_response