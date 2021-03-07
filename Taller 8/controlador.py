from app import app
from modelos import *
from flask import render_template

@app.route('/')
def index():
    persona=persona.query.all()
    ciudad=ciudad.query.all()
    tipodocumento=tipodocumento.query.all()
    return render_template('index.html')
    