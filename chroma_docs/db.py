import os
import chromadb

chroma_client = chromadb.HttpClient(host='localhost', port=8000)

def import_documents(ef):
  documents = []
  files = os.listdir("docs")
  for filename in files:
    with open(f"docs/{filename}", "r") as file:
      for line_number, line in enumerate(file.readlines()):
        line = line.strip()
        if len(line) == 0:
            continue
        documents.append(line)

  collection = chroma_client.get_or_create_collection(name="api_docs", embedding_function=ef)
  ids = [str(i) for i in range(0, len(documents))]
  collection.add(
    documents=documents,
    ids=ids,
  )

  return collection
  