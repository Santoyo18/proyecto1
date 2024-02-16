from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import celador_routes, detallesalida_routes,pc_routes,salidaequipo_routes,usuario_routes,session_routes
