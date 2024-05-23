from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from src.models import Cliente
from src.app import db

auth_bp = Blueprint('auth', __name__)

#Metodo registro
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    cedula = data.get('cedula')
    correo = data.get('correo')
    telefono = data.get('telefono')
    contraseña = data.get('contraseña')

    if not (nombre and apellido and cedula and correo and telefono and contraseña):
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400
    
    if Cliente.query.filter_by(correo=correo).first():
        return jsonify({'error': 'El correo ya esta registrado'}), 409
    
    hashed_password = generate_password_hash(contraseña, method='pbkdf2:sha256')
    nuevo_cliente = Cliente(
        nombre=nombre,
        apellido=apellido,
        cedula=cedula,
        correo=correo,
        telefono=telefono,
        contraseña=hashed_password
    )
    try:
        db.session.add(nuevo_cliente)
        db.session.commit()
        return jsonify({'message': 'Cliente registrado con éxito'}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'No se pudo registrar al cliente', 'detalle': str(e)}), 500

#Metodo login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    correo = data.get('correo')
    contraseña = data.get('contraseña')

    if not(correo and contraseña):
        return jsonify({'error': 'Correo y contraseña son obligatorios'}), 400
    
    cliente = Cliente.query.filter_by(correo = correo).first()

    if cliente and check_password_hash(cliente.contraseña, contraseña):
        access_token = create_access_token(identity=cliente.idCliente)
        return jsonify({'message': 'Inicio de sesion exitoso', 'access_token': access_token}), 200
    
    return jsonify({'error': 'Credenciales inválidas'}), 401

#Metodo logout
@auth_bp.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    return jsonify({'message': 'Sesión cerrada exitosamente'}), 200
