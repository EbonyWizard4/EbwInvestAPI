"""Primeira pagina em Flask
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    """Primeira página em Flask
    Returns:
        HTML: Conteudo da pagina
    """
    return render_template("index.html")
