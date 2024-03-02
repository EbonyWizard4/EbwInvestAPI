from .models.pokemon import Pokemon
from flask.globals import request
from app import app
from flask import render_template


@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/buscar', methods = ['GET', 'post'])
def buscar():
    pokemon = Pokemon(request.form['nome'],"")
