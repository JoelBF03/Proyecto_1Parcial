#src/routes/cliente_route.py
from flask import Blueprint, request, jsonify
from src.models import Cliente
from src.app import db

cliente_bp = Blueprint('cliente', __name__)

#GET - OBTENER TODOS LOS CLIENTES
@cliente_bp.route('/cliente', methods=['GET'])
def get_clientes():
    try:
        clientes = Cliente.query.order_by(Cliente.idCliente.asc()).all()
        serialized_clientes = [cliente.serialize() for cliente in clientes]
        return jsonify(serialized_clientes), 200
    except Exception as e:
        print("Error al obtener los clientes:", str(e))
        return jsonify({'error': 'No se pudo obtener los clientes'}), 500

#GET - OBTENER UN CLIENTE POR SU ID
@cliente_bp.route('/cliente/<int:id>', methods=['GET'])
def get_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if cliente:
            return jsonify(cliente.serialize()), 200
        else:
            return jsonify({'error': 'Cliente no encontrado'}), 404
    except Exception as e:
        print("Error al obtener el cliente:", str(e))
        return jsonify({'error': 'No se pudo obtener el cliente'}), 500
    

#POST - CREAR UN NUEVO CLIENTE
@cliente_bp.route('/cliente', methods=['POST'])
def create_cliente():
    try:
        data = request.json
        nuevo_cliente = Cliente(
            nombre=data['nombre'],
            apellido=data['apellido'],
            cedula=data['cedula'],
            correo=data['correo'],
            telefono=data['telefono']
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return jsonify(nuevo_cliente.serialize()), 201
    except Exception as e:
        db.session.rollback()
        print("Error al crear el cliente:", str(e))
        return jsonify({'error': 'No se pudo crear el cliente'}), 500 

#PUT - ACTUALIZAR UN CLIENTE EXISTENTE
@cliente_bp.route('/cliente/<int:id>', methods=['PUT'])
def update_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({'error': 'Cliente no encontrado'}), 404

        data = request.json
        updatable_fields = ['nombre', 'apellido', 'cedula', 'correo', 'telefono'] # Atributos permitidos para la actualización

        for field in updatable_fields:
            if field in data:
                setattr(cliente, field, data[field]) # Actualiza solo los campos proporcionados en la solicitud

        db.session.commit()
        return jsonify(cliente.serialize()), 200
    except Exception as e:
        db.session.rollback()
        print("Error al actualizar el cliente:", str(e))
        return jsonify({'error': 'No se pudo actualizar el cliente'}), 500

#DELETE - ELIMINAR UN CLIENTE POR SU ID
@cliente_bp.route('/cliente/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            return jsonify({'message': 'Cliente eliminado correctamente'}), 200
        else:
            return jsonify({'message': 'Cliente no encontrado'}), 404
    except Exception as e:
        db.session.rollback()
        print("Error al eliminar el cliente:", str(e))
        return jsonify({'error': 'No se pudo eliminar el cliente'}), 500
