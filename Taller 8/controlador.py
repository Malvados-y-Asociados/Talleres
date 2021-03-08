from app import app
from modelos import *
from flask import render_template, request, redirect, url_for


@app.route('/')
def index():
    personas = persona.query.all()
    personass=[]
    for Persona in personas:
        personass += [Persona]

    return render_template('Vista.html',list=personass)


@app.route('/registros', methods=['POST'])
def registros():
    perso = persona(nombres=request.form['nombres'], apellidos=request.form['apellidos'],
                      idtipodocumento=request.form['tipodocumento'], documento=request.form['documento'], lugarresidencia=request.form['residencia'],
                      fechanacimiento=request.form['fecha'], email=request.form['email'], telefono=request.form['telefono'], usuario=request.form['usuario'],
                      password=request.form['password'])
    db.session.add(perso)
    db.commit
    return redirect(url_for('index'))
