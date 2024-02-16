from flask import Blueprint, request, render_template,redirect,url_for
from app import db
from app.models.Pc import Pc

bp = Blueprint('Pc', __name__)

@bp.route('/Pc', methods=['GET', 'POST'])
def index():
    return render_template("Pc.html")

@bp.route('/nosotros', methods=['GET'])
def XD():
    return render_template("nosotros.html")

@bp.route('/Pc2', methods=['GET'])
def XD2():
    data = Pc.query.all()
    return render_template("lista.html", data=data)

@bp.route('/Pc/add', methods=['POST'])
def add():
    try:
        marca = request.form.get('marca')
        codigo = request.form.get('codigo')
        color = request.form.get('color')
        desp = request.form.get('desp')
        estado = request.form.get('estado')
        estado = estado == '1'

        new_Pc = Pc(marca=marca, codigo=codigo, color=color, desp=desp, estado=estado)
        db.session.add(new_Pc)
        db.session.commit()
        return redirect(url_for('Pc.index')) 
        
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar Pc: {str(e)}", 500

@bp.route('/Pc/edit/<int:id>', methods=['POST'])
def edit(id):
    try:
        pc = Pc.query.get_or_404(id)
        if pc:
            pc.estado = False
            db.session.commit()
            return redirect(url_for('Pc.XD2'))
        else:
            return "Pc no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar Pc: {str(e)}", 500

@bp.route('/Pc/editt/<int:id>', methods=['POST'])
def editt(id):
    try:
        pc = Pc.query.get_or_404(id)
        if pc:
            pc.estado = True
            db.session.commit()
            return redirect(url_for('Pc.XD2'))
        else:
            return "Pc no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar Pc: {str(e)}", 500
@bp.route('/Pc/delete/<int:id>', methods=['POST'])
def delete(id):
    try:
        pc= Pc.query.get_or_404(id)

        if pc:
            db.session.delete(pc)
            db.session.commit()
            return redirect(url_for('Pc.XD2'))
        else:
            return "Pc no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar Pc: {str(e)}", 500
    
