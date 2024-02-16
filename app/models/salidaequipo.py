from app import db

class SalidaEquipo(db.Model):
    __tablename__ = 'salida_Pc'
    idSalida = db.Column(db.Integer, primary_key=True)
    fechaSalida = db.Column(db.String(45))
    idusuario = db.Column(db.Integer, db.ForeignKey('usuario.idusuario'))
    idCelador = db.Column(db.Integer, db.ForeignKey('Celador.idCelador'))
    usuario = db.relationship("Usuario")