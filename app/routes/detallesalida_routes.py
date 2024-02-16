from flask import Blueprint, request, render_template
from app import db
from app.models.detallesalida import DetalleSalida
from app.models.Pc import Pc


bp = Blueprint('detalle_salida', __name__)

@bp.route('/detallesalida', methods=['GET', 'POST'])
def index():
    data = DetalleSalida.query.all()
    data1 = Pc.query.all()
    return render_template("devolucion.html", data=data ,data1=data1)

@bp.route('/detallesalida/add', methods=['POST'])
def add():
    try:
        
        fechaEntregaDetalleSalida=request.form.get('fechaEntregaDetalleSalida')
        idSalida=request.form.get('idSalida')
        idequipo=request.form.get('idequipo')
        
        new_detalle_salida = DetalleSalida(fechaEntregaDetalleSalida=fechaEntregaDetalleSalida,idSalida=idSalida,idequipo=idequipo)
        db.session.add(new_detalle_salida)
        db.session.commit()
        return render_template("devolucion.html")
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar detalle de salida: {str(e)}", 500

@bp.route('/detallesalida/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        detalle_salida = db.session.query(DetalleSalida).get(id)
        if detalle_salida:
            fechaEntregaDetalleSalida=request.form.get('fechaEntregaDetalleSalida')
            idSalida=request.form.get('idSalida')
            idequipo=request.form.get('idequipo')
        
            id = DetalleSalida(fechaEntregaDetalleSalida=fechaEntregaDetalleSalida,idSalida=idSalida,idequipo=idequipo)
            db.session.commit()
            return render_template("devolucion.html")
        else:
            return "Detalle de salida no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar detalle de salida: {str(e)}", 500

@bp.route('/detallesalida/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        detalle_salida = db.session.query(DetalleSalida).get(id)
        if detalle_salida:
            db.session.delete(detalle_salida)
            db.session.commit()
            return "Detalle de salida eliminado correctamente", 200
        else:
            return "Detalle de salida no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar detalle de salida: {str(e)}", 500