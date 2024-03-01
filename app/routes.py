from app import app
from flask import render_template

@app.route('/')

@app.route('/index')
def index():
    nome = 'Jhone'
    return render_template('index.html', nome=nome)

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')