from app import app
from modelos import *
from flask import render_template


@app.route('/')
def index():
    personas = persona.query_all()
    ciudades = ciudad.query_all()
    tiposdocumentos = tipodocumento.query_all()
    personass=[]
    ciudadess=[]
    tiposdocumentoss=[]
    for persona in personas:
        personass += [persona]
        
    for ciudad in ciudades:
        ciudadess += [ciudad]

    for tipodocumento in tiposdocumentos:
        tiposdocumentoss += [tipodocumento]

    return render_template('index.html',personass,ciudadess,tiposdocumentoss)
    