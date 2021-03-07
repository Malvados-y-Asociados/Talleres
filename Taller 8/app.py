from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET KEY'] = 'Tigris'
app.config['SQLALCHEMY_DATABASES_URI'] = 'sqlite:///databases/proyecto.db'

db = SQLAlchemy(app)

from controlador import *

if __name__ == '__main__':
    app.run(debug=True)