from app import db

class persona(db.Model):
    __tablename__ = 'Persona'
    id = db.Column(db.Integer, primary_key = True)
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
#    idtipodocumento = db.Column(db.Integer, foreignKey('tipodocumento.id'))
    documento = db.Column(db.Integer)
#    lugarresidencia = db.Column(db.String(100), foreignKey('ciudad.id'))
    email = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    usuario = db.Column(db.String(50))
    password = db.Column(db.String(50))


class tipodocumento(db.Model):
    __tablename__ = 'Tipo de Documento'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
#    persona = relationship('Persona')


class ciudad(db.Model):
    __tablename__ = 'Ciudad'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
#    persona = relationship('Persona')
