"""Primeira pagina em Flask
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  """Primeira página em Flask
  Returns:
      HTML: Conteudo da pagina
  """
  return "<H1>Hello World</H1>"
