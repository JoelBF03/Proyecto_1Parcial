from flask import Blueprint, request, jsonify
from src.models import PedidoServicio, Pedido, TipoServicio
from src.app import db

pedidoservicio_bp = Blueprint('pedido_servicio', __name__)

# GET - OBTENER TODOS LOS PEDIDOS SERVICIOS
@pedidoservicio_bp.route('/pedido_servicio', methods=['GET'])
def get_pedidos_servicios():
    try:
        pedidos_servicios = PedidoServicio.query.all()
        serialized_pedidos_servicios = [pedido_servicio.serialize() for pedido_servicio in pedidos_servicios]
        return jsonify(serialized_pedidos_servicios), 200
    except Exception as e:
        print("Error al obtener los pedidos servicios:", str(e))
        return jsonify({'error': 'No se pudo obtener los pedidos servicios'}), 500

# GET - OBTENER UN PEDIDO SERVICIO POR SU ID
@pedidoservicio_bp.route('/pedido_servicio/<int:id>', methods=['GET'])
def get_pedido_servicio(id):
    try:
        pedido_servicio = PedidoServicio.query.get(id)
        if pedido_servicio:
            return jsonify(pedido_servicio.serialize()), 200
        else:
            return jsonify({'error': 'Pedido Servicio no encontrado'}), 404
    except Exception as e:
        print("Error al obtener el pedido servicio:", str(e))
        return jsonify({'error': 'No se pudo obtener el pedido servicio'}), 500

# POST - CREAR UN NUEVO PEDIDO SERVICIO
@pedidoservicio_bp.route('/pedido_servicio', methods=['POST'])
def create_pedido_servicio():
    try:
        data = request.json
        nuevo_pedido_servicio = PedidoServicio(
            cantidad=data['cantidad'],
            descripcion=data['descripcion'],
            idPedido=data['idPedido'],
            idTipo_servicio=data['idTipo_servicio']
        )
        db.session.add(nuevo_pedido_servicio)
        db.session.commit()
        return jsonify(nuevo_pedido_servicio.serialize()), 201
    except Exception as e:
        db.session.rollback()
        print("Error al crear el pedido servicio:", str(e))
        return jsonify({'error': 'No se pudo crear el pedido servicio'}), 500

# PUT - ACTUALIZAR UN PEDIDO SERVICIO EXISTENTE
@pedidoservicio_bp.route('/pedido_servicio/<int:id>', methods=['PUT'])
def update_pedido_servicio(id):
    try:
        pedido_servicio = PedidoServicio.query.get(id)
        if not pedido_servicio:
            return jsonify({'error': 'Pedido Servicio no encontrado'}), 404

        data = request.json
        updatable_fields = ['cantidad', 'descripcion', 'idPedido', 'idTipo_servicio'] # Atributos permitidos para la actualización        
        for field in updatable_fields:
            if field in data:
                setattr(pedido_servicio, field, data[field]) # Actualiza solo los campos proporcionados en la solicitud

        db.session.commit()
        return jsonify(pedido_servicio.serialize()), 200
    except Exception as e:
        db.session.rollback()
        print("Error al actualizar el pedido servicio:", str(e))
        return jsonify({'error': 'No se pudo actualizar el pedido servicio'}), 500

# DELETE - ELIMINAR UN PEDIDO SERVICIO POR SU ID
@pedidoservicio_bp.route('/pedido_servicio/<int:id>', methods=['DELETE'])
def delete_pedido_servicio(id):
    try:
        pedido_servicio = PedidoServicio.query.get(id)
        if pedido_servicio:
            db.session.delete(pedido_servicio)
            db.session.commit()
            return jsonify({'message': 'Pedido Servicio eliminado correctamente'}), 200
        else:
            return jsonify({'error': 'Pedido Servicio no encontrado'}), 404
    except Exception as e:
        db.session.rollback()
        print("Error al eliminar el pedido servicio:", str(e))
        return jsonify({'error': 'No se pudo eliminar el pedido servicio'}), 500