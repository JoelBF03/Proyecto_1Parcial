from flask import Blueprint, jsonify
from src.models import MetodoPago
from flask_jwt_extended import jwt_required

metodopago_bp = Blueprint('metodo_pago', __name__)

# GET - OBTENER TODOS LOS METODOS DE PAGO
@metodopago_bp.route('/metodo_pago', methods=['GET'])
@jwt_required()
def get_metodos_pago():
    try:
        metodos_pago = MetodoPago.query.order_by(MetodoPago.idMetodo_pago.asc()).all()
        serialized_metodos_pago = [metodo.serialize() for metodo in metodos_pago]
        return jsonify(serialized_metodos_pago), 200
    except Exception as e:
        print("Error al obtener los métodos de pago:", str(e))
        return jsonify({'error': 'No se pudo obtener los métodos de pago'}), 500

"""
# POST - CREAR UN NUEVO METODO DE PAGO
@metodopago_bp.route('/metodo_pago', methods=['POST'])
def create_metodo_pago():
    try:
        data = request.json
        nuevo_metodo_pago = MetodoPago(
            descripcion=data['descripcion']
        )
        db.session.add(nuevo_metodo_pago)
        db.session.commit()
        return jsonify(nuevo_metodo_pago.serialize()), 201
    except Exception as e:
        db.session.rollback()
        print("Error al crear el método de pago:", str(e))
        return jsonify({'error': 'No se pudo crear el método de pago'}), 500
    
# PUT - ACTUALIZAR UN METODO DE PAGO EXISTENTE
@metodopago_bp.route('/metodo_pago/<int:id>', methods=['PUT'])
def update_metodo_pago(id):
    try:
        metodo_pago = MetodoPago.query.get(id)
        if not metodo_pago:
            return jsonify({'error': 'Metodo de pago no encontrado'}), 404

        data = request.json
        updatable_fields = ['descripcion'] # Atributos permitidos para la actualización
        for field in updatable_fields:
            if field in data:
                setattr(metodo_pago, field, data[field]) # Actualiza solo los campos proporcionados en la solicitud

        db.session.commit()
        return jsonify(metodo_pago.serialize()), 200
    except Exception as e:
        db.session.rollback()
        print("Error al actualizar el metodo de pago:", str(e))
        return jsonify({'error': 'No se pudo actualizar el metodo de pago'}), 500

# DELETE - ELIMINAR UN METODO DE PAGO POR SU ID
@metodopago_bp.route('/metodo_pago/<int:id>', methods=['DELETE'])
def delete_metodo_pago(id):
    try:
        metodo_pago = MetodoPago.query.get(id)
        if not metodo_pago:
            return jsonify({'error': 'Metodo de pago no encontrado'}), 404

        db.session.delete(metodo_pago)
        db.session.commit()

        return jsonify({'message': 'Metodo de pago eliminado correctamente'}), 200
    except Exception as e:
        db.session.rollback()
        print("Error al eliminar el método de pago:", str(e))
        return jsonify({'error': 'No se pudo eliminar el método de pago'}), 500
     """