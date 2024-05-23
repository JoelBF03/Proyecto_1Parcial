# src/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from src.config import *

app = Flask(__name__)
app.config.from_object('src.config')

# Crear una instancia de SQLAlchemy
db = SQLAlchemy(app)

# Crear una instancia de Migrate
migrate = Migrate(app, db)

# Importar los modelos después de crear db para que SQLAlchemy los reconozca
from src.models import *

# Inicializar Flask-JWT-Extended
jwt = JWTManager(app)

# Inicializar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Cliente.query.get(int(user_id))

# Importar y registrar blueprints después de inicializar los componentes
from src.routes.cliente_route import cliente_bp
from src.routes.metodo_pago_route import metodopago_bp
from src.routes.tipo_servicio_route import tiposervicio_bp
from src.routes.pedido_route import pedido_bp
#from src.routes.pedido_servicio_route import pedidoservicio_bp
from src.controllers.auth_controller import auth_bp

app.register_blueprint(cliente_bp)
app.register_blueprint(metodopago_bp)
app.register_blueprint(tiposervicio_bp)
app.register_blueprint(pedido_bp)
#app.register_blueprint(pedidoservicio_bp)
app.register_blueprint(auth_bp)

print(app.url_map)

# Función para inicializar las migraciones
def initialize_migrations():
    from flask.cli import FlaskGroup

    flask_group = FlaskGroup(app)
    flask_group.main(['db', 'init'])

if __name__ == '__main__':
    initialize_migrations()
    app.run(debug=True)
