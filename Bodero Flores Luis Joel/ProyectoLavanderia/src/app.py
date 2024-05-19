# src/app.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src import app

# Configurar conexión a la base de datos
USER_DB = 'postgres'
PASS_DB = '092218'
URL_DB = 'localhost'
NAME_DB = 'proyecto_lavanderia'

# Crear una cadena de conexión completa para la bd
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

# Configurar las variables para que SQLAlchemy funcione con Flask
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear una instancia de SQLAlchemy
db = SQLAlchemy(app)

# Crear una instancia de Migrate
migrate = Migrate(app, db)

# Importar los modelos después de crear db para que SQLAlchemy los conozca
from src.models import *

# Definir una función para inicializar las migraciones
def initialize_migrations():
    from flask.cli import FlaskGroup

    flask_group = FlaskGroup(app)
    flask_group.main(['db', 'init'])

# Si ejecutas db.py directamente, inicializa las migraciones
if __name__ == '__main__':
    initialize_migrations()
