from app import db
from flask_login import UserMixin

class Celador(db.Model,UserMixin):
    __tablename__ = 'Celador'
    idCelador = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(45))
    nombre = db.Column(db.String(45))
    Aprellido = db.Column(db.String(45))
    telefono = db.Column(db.String(45))
    contraseña = db.Column(db.String(45))

    def get_id(self):
        return self.idCelador   