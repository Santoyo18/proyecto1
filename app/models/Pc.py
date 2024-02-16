from app import db


class Pc(db.Model):
    __tablename__ = 'Pc'
    idPc = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(45))
    codigo = db.Column(db.String(45))
    color = db.Column(db.String(45))
    desp = db.Column(db.String(45))
    estado = db.Column(db.Boolean)