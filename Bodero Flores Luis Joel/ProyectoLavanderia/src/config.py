# src/config.py
USER_DB = 'postgres'
PASS_DB = '092218'
URL_DB = 'localhost'
NAME_DB = 'proyecto_lavanderia'

SECRET_KEY = 'mi_secreto_super_secreto'
JWT_SECRET_KEY = 'HESOYAM_123'

SQLALCHEMY_DATABASE_URI = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
