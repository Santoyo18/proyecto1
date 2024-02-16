from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config["SECRET_KEY"]= os.urandom(24)

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(idCelador):
        from app.models.Celador import Celador
        Celador = Celador.query.get(int(idCelador))
        return Celador

    from app.routes import celador_routes, detallesalida_routes,pc_routes,salidaequipo_routes,usuario_routes,session_routes
    app.register_blueprint(celador_routes.bp)
    app.register_blueprint(detallesalida_routes.bp)
    app.register_blueprint(pc_routes.bp)
    app.register_blueprint(salidaequipo_routes.bp)
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(session_routes.auth_bp)

    return app