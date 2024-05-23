#src/routes/cliente_route.py
from flask import Blueprint, request, jsonify
from src.models import Cliente
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.app import db

cliente_bp = Blueprint('cliente', __name__)

#GET - OBSERVAR DATOS DEL CLIENTE
@cliente_bp.route('/cliente', methods=['GET'])
@jwt_required()
def get_clientes():
    try:
        cliente_id = get_jwt_identity()
        cliente = Cliente.query.get(cliente_id)
        if not cliente:
            return jsonify({'error': 'Cliente no encontrado'}), 404
        
        return jsonify(cliente.serialize()), 200

    except Exception as e:
        print("Error al obtener el cliente:", str(e))
        return jsonify({'error': 'No se pudo obtener el cliente'}), 500

#PUT - ACTUALIZAR DATOS
@cliente_bp.route('/cliente', methods=['PUT'])
@jwt_required()
def update_cliente():
    try:
        cliente_id = get_jwt_identity()
        cliente = Cliente.query.get(cliente_id)
        if not cliente:
            return jsonify({'error': 'Cliente no encontrado'}), 404

        data = request.json
        updatable_fields = ['nombre', 'apellido', 'telefono'] # Atributos permitidos para la actualización

        for field in updatable_fields:
            if field in data:
                setattr(cliente, field, data[field]) # Actualiza solo los campos proporcionados en la solicitud

        db.session.commit()
        return jsonify(cliente.serialize()), 200
    except Exception as e:
        db.session.rollback()
        print("Error al actualizar el cliente:", str(e))
        return jsonify({'error': 'No se pudo actualizar el cliente'}), 500

#DELETE - ELIMINAR CUENTA
@cliente_bp.route('/cliente', methods=['DELETE'])
@jwt_required()
def delete_cliente():
    try:
        cliente_id = get_jwt_identity()
        cliente = Cliente.query.get(cliente_id)
        if not cliente:
            return jsonify({'error': 'Cliente no encontrado'}), 404
        
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({'message': 'Cuenta eliminada correctamente'}), 200
    except Exception as e:
        db.session.rollback()
        print("Error al eliminar el cliente:", str(e))
        return jsonify({'error': 'No se pudo eliminar el cliente'}), 500
