from flask import Blueprint, request, render_template
from app import db
from app.models.usuario import Usuario 

bp = Blueprint('usuario', __name__)

@bp.route('/Registar', methods=['GET', 'POST'])
def reg():
    return render_template("registrar.html")

@bp.route('/usuario', methods=['GET', 'POST'])
def index():
    data = Usuario.query.all()
    return render_template("usuario.html", data=data)

@bp.route('/usuario/add', methods=['POST'])
def add():
    try:
        nombre=request.form.get('nombre')
        correo=request.form.get('correo')

        new_usuario = Usuario(nombre=nombre,correo=correo)
        db.session.add(new_usuario)
        db.session.commit()
        return render_template("welcome.html")
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar usuario: {str(e)}", 500

@bp.route('/usuario/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        usuario = db.session.query(Usuario).get(id)
        if usuario:
            nombre=request.form.get('nombre')
            correo=request.form.get('correo')

            id = usuario(nombre=nombre,correo=correo)
            db.session.commit()
            return render_template("welcome.html")
        else:
            return "Usuario no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar usuario: {str(e)}", 500

@bp.route('/usuario/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        usuario = db.session.query(Usuario).get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return "Usuario eliminado correctamente", 200
        else:
            return "Usuario no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar usuario: {str(e)}", 500    
    
@bp.route('/registrar')  # Añadir corchetes alrededor de 'POST'
def inicio():
    return render_template("registrar.html")