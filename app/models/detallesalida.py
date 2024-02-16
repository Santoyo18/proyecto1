from app import db

class DetalleSalida(db.Model):
    __tablename__ = 'detalle_salida'
    idDetalleSalida = db.Column(db.Integer, primary_key=True)
    fechaEntregaDetalleSalida = db.Column(db.String(45))
    idSalida = db.Column(db.Integer, db.ForeignKey('salida_Pc.idSalida'))
    idPc = db.Column(db.Integer, db.ForeignKey('Pc.idPc'))