from flask import current_app, Blueprint, render_template, request

from .OpenAIClient import OpenAIClient
from .db import import_documents, chroma_client

bp = Blueprint('v1', __name__, url_prefix='')
openai_client = OpenAIClient()
collection = import_documents(ef=openai_client.ef)

@bp.route("/")
def index():
  return render_template('index.html')

@bp.route("/query")
def query_docs():
  query = request.args.get("query")

  results = collection.query(
    query_texts=[query], n_results=20, include=["documents"]
  )

  response = openai_client.query_gpt(query, results["documents"][0])
  
  return response
