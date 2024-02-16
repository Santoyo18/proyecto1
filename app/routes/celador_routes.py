from flask import Blueprint, request, render_template
from app import db
from app.models.Celador import Celador 

bp = Blueprint('Celador', __name__)

@bp.route('/')
def index():
    data = Celador.query.all()
    return render_template("index.html", data=data)

@bp.route('/add', methods=['POST'])
def add():
    try:
        cedula=request.form.get('cedula')
        nombre=request.form.get('nombre')
        Aprellido=request.form.get('Aprellido')
        telefono=request.form.get('telefono')
        contraseña=request.form.get('contraseña')
        
        new_admin = Celador(cedula=cedula,nombre=nombre,Aprellido=Aprellido,telefono=telefono,contraseña=contraseña)
        db.session.add(new_admin)
        db.session.commit()
        return render_template("index.html")
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar Celador: {str(e)}", 500

@bp.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        admin = db.session.query(Celador).get(id)
        if admin:
            cedula=request.form.get('cedula')
            nombre=request.form.get('nombre')
            Aprellido=request.form.get('Aprellido')
            telefono=request.form.get('telefono')
            contraseña=request.form.get('contraseña')
        
            id = Celador(cedula=cedula,nombre=nombre,Aprellido=Aprellido,telefono=telefono,contraseña=contraseña)
            db.session.commit()
            return render_template("welcome.html")
        else:
            return "Celador no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar Celador: {str(e)}", 500

@bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        admin = db.session.query(Celador).get(id)
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return "Celador eliminado correctamente", 200
        else:
            return "Celador no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar Celador: {str(e)}", 500
