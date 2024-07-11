import os
import chromadb.utils.embedding_functions as embedding_functions

from openai import OpenAI

class OpenAIClient:
  def __init__(self):
    self.ef = embedding_functions.OpenAIEmbeddingFunction(
      api_key=os.environ["OPENAI_API_KEY"],
      model_name="text-embedding-3-small"
    )
    self.client = OpenAI()

  def query_gpt(self, query, context):
    response = self.client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=self.prompt(query, context)
    )

    return response.choices[0].message.content

  def prompt(self, query, context):
    system_prompt = {
      "role": "system",
      "content": "You are a software engineer tasked with reading and parsing the API docs of a new vector database called Chroma."
      "The docs are in markdown format."
      "You need to digest questions about the database based on the provided context and not any other knowledge."
      "If you don't have enough information to give an anser, say 'I don't have enough information to answer this question.'"
    }

    user_prompt = {
      "role": "user",
      "content": f"The query is: {query}. The context is: {context}"
    }

    return [system_prompt, user_prompt]