""" 
#RUTA SOLO APTO PARA ADMINISTRADORES

from flask import Blueprint, request, jsonify
from src.models import PedidoServicio, Pedido, TipoServicio
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.app import db

pedidoservicio_bp = Blueprint('pedido_servicio', __name__)

# GET - OBTENER TODOS LOS PEDIDOS SERVICIOS DEL CLIENTE AUTENTICADO
@pedidoservicio_bp.route('/pedido_servicio', methods=['GET'])
@jwt_required()
def get_pedidos_servicios():
    try:
        cliente_id = get_jwt_identity()
        # Obtener todos los pedidos del cliente autenticado
        pedidos = Pedido.query.filter_by(idCliente=cliente_id).all()
        pedido_ids = [pedido.idPedido for pedido in pedidos]
        
        # Obtener todos los PedidoServicio asociados a los pedidos del cliente
        pedido_servicios = PedidoServicio.query.filter(PedidoServicio.idPedido.in_(pedido_ids)).all()
        serialized_pedido_servicios = [ps.serialize() for ps in pedido_servicios]
        return jsonify(serialized_pedido_servicios), 200
    except Exception as e:
        print("Error al obtener los pedido_servicio:", str(e))
        return jsonify({'error': 'No se pudo obtener los pedido_servicio'}), 500


# GET - OBTENER UN PEDIDO SERVICIO POR SU ID
@pedidoservicio_bp.route('/pedido_servicio/<int:id>', methods=['GET'])
@jwt_required()
def get_pedido_servicio_by_id(id):
    try:
        cliente_id = get_jwt_identity()
        pedido_servicio = PedidoServicio.query.get(id)
        if not pedido_servicio:
            return jsonify({'error': 'Pedido_Servicio no encontrado'}), 404

        pedido = Pedido.query.get(pedido_servicio.idPedido)
        if not pedido or pedido.idCliente != cliente_id:
            return jsonify({'error': 'Pedido_Servicio no autorizado'}), 403

        return jsonify(pedido_servicio.serialize()), 200
    except Exception as e:
        print("Error al obtener el pedido_servicio:", str(e))
        return jsonify({'error': 'No se pudo obtener el pedido_servicio'}), 500

# POST - CREAR UN NUEVO PEDIDO SERVICIO
@pedidoservicio_bp.route('/pedido_servicio', methods=['POST'])
@jwt_required()
def create_pedido_servicio():
    try:
        cliente_id = get_jwt_identity()
        data = request.json

        pedido = Pedido.query.get(data.get('idPedido'))
        if not pedido or pedido.idCliente != cliente_id:
            return jsonify({'error': 'Pedido no encontrado o no autorizado'}), 403

        nuevo_pedido_servicio = PedidoServicio(
            cantidad=data.get('cantidad'),
            descripcion=data.get('descripcion'),
            idPedido=data.get('idPedido'),
            idTipo_servicio=data.get('idTipo_servicio')
        )

        db.session.add(nuevo_pedido_servicio)
        db.session.commit()

        return jsonify(nuevo_pedido_servicio.serialize()), 201
    except Exception as e:
        db.session.rollback()
        print("Error al crear el pedido_servicio:", str(e))
        return jsonify({'error': 'No se pudo crear el pedido_servicio'}), 500

# PUT - ACTUALIZAR UN PEDIDO SERVICIO EXISTENTE
@pedidoservicio_bp.route('/pedido_servicio/<int:id>', methods=['PUT'])
@jwt_required()
def update_pedido_servicio(id):
    try:
        cliente_id = get_jwt_identity()
        pedido_servicio = PedidoServicio.query.get(id)
        if not pedido_servicio:
            return jsonify({'error': 'Pedido_Servicio no encontrado'}), 404

        pedido = Pedido.query.get(pedido_servicio.idPedido)
        if not pedido or pedido.idCliente != cliente_id:
            return jsonify({'error': 'Pedido_Servicio no autorizado'}), 403

        data = request.json
        updatable_fields = ['cantidad', 'descripcion', 'idTipo_servicio']
        for field in updatable_fields:
            if field in data:
                setattr(pedido_servicio, field, data[field])

        db.session.commit()
        return jsonify(pedido_servicio.serialize()), 200
    except Exception as e:
        db.session.rollback()
        print("Error al actualizar el pedido_servicio:", str(e))
        return jsonify({'error': 'No se pudo actualizar el pedido_servicio'}), 500

# DELETE - ELIMINAR UN PEDIDO SERVICIO POR SU ID
@pedidoservicio_bp.route('/pedido_servicio/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_pedido_servicio(id):
    try:
        cliente_id = get_jwt_identity()
        pedido_servicio = PedidoServicio.query.get(id)
        if not pedido_servicio:
            return jsonify({'error': 'Pedido_Servicio no encontrado'}), 404

        pedido = Pedido.query.get(pedido_servicio.idPedido)
        if not pedido or pedido.idCliente != cliente_id:
            return jsonify({'error': 'Pedido_Servicio no autorizado'}), 403

        db.session.delete(pedido_servicio)
        db.session.commit()
        return jsonify({'message': 'Pedido_Servicio eliminado correctamente'}), 200
    except Exception as e:
        db.session.rollback()
        print("Error al eliminar el pedido_servicio:", str(e))
        return jsonify({'error': 'No se pudo eliminar el pedido_servicio'}), 500
    
     """