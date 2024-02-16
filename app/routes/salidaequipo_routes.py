from flask import Blueprint, request, render_template
from app import db
from app.models.salidaequipo import SalidaEquipo

bp = Blueprint('salida_equipo', __name__)

@bp.route('/salidaequipo', methods=['GET', 'POST'])
def index():
    data = SalidaEquipo.query.all()
    return render_template("prestamo.html", data=data)

@bp.route('/salidaequipo/add', methods=['POST'])
def add():
    try:
        fechaSalida=request.form.get('fechaSalida')
        idusuario=request.form.get('idusuario')
        idCelador=request.form.get('idCelador')

        new_salida_equipo = SalidaEquipo(fechaSalida=fechaSalida, idusuario=idusuario, idCelador=idCelador)
        db.session.add(new_salida_equipo)
        db.session.commit()
        return render_template("prestamo.html")
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar salida de equipo: {str(e)}", 500

@bp.route('/salidaequipo/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        salida_equipo = db.session.query(SalidaEquipo).get(id)
        if salida_equipo:
            fechaSalida=request.form.get('fechaSalida')
            idusuario=request.form.get('idusuario')
            idCelador=request.form.get('idCelador')

            id = SalidaEquipo(fechaSalida=fechaSalida, idusuario=idusuario, idCelador=idCelador)
            db.session.commit()
            return render_template("prestamo.html")
        else:
            return "Salida de equipo no encontrada", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar salida de equipo: {str(e)}", 500

@bp.route('/salidaequipo/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        salida_equipo = db.session.query(SalidaEquipo).get(id)
        if salida_equipo:
            db.session.delete(salida_equipo)
            db.session.commit()
            return "Salida de equipo eliminada correctamente", 200
        else:
            return "Salida de equipo no encontrada", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar salida de equipo: {str(e)}", 500
