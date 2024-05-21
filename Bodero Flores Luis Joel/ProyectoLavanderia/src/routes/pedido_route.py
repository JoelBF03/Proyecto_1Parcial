from flask import Blueprint, request, jsonify
from src.models import Pedido, Cliente, MetodoPago
from src.app import db

pedido_bp = Blueprint('pedido', __name__)

#GET - OBTENER TODOS LOS PEDIDOS
@pedido_bp.route('/pedido', methods=['GET'])
def get_pedidos():
    try:
        pedidos = Pedido.query.all()
        serialized_pedidos = [pedido.serialize() for pedido in pedidos]
        return jsonify(serialized_pedidos), 200
    except Exception as e:
        print("Error al obtener los pedidos:", str(e))
        return jsonify({'error': 'No se pudo obtener los pedidos'}), 500

# GET - OBTENER UN PEDIDO POR SU ID
@pedido_bp.route('/pedido/<int:id>', methods=['GET'])
def get_pedido_by_id(id):
    try:
        pedido = Pedido.query.get(id)
        if not pedido:
            return jsonify({'error': 'Pedido no encontrado'}), 404
        
        # Incluir detalles de cliente y método de pago en la respuesta
        serialized_pedido = pedido.serialize()
        serialized_pedido['cliente'] = pedido.cliente.serialize()
        serialized_pedido['metodo_pago'] = pedido.metodo_pago.serialize()

        return jsonify(serialized_pedido), 200
    except Exception as e:
        print("Error al obtener el pedido:", str(e))
        return jsonify({'error': 'No se pudo obtener el pedido'}), 500
    
# POST - CREAR UN NUEVO PEDIDO
@pedido_bp.route('/pedido', methods=['POST'])
def create_pedido():
    try:
        data = request.json

        # Crear nuevo pedido con los datos proporcionados
        nuevo_pedido = Pedido(
            pedido_ropa=data.get('pedido_ropa'),
            pedido_cantidad=data.get('pedido_cantidad'),
            observacion=data.get('observacion'),
            fecha_servicio=data.get('fecha_servicio'),
            idCliente=data.get('idCliente'),
            idMetodo_pago=data.get('idMetodo_pago')
        )
        
        db.session.add(nuevo_pedido)
        db.session.commit()

        return jsonify(nuevo_pedido.serialize()), 201
    except Exception as e:
        db.session.rollback()
        print("Error al crear el pedido:", str(e))
        return jsonify({'error': 'No se pudo crear el pedido'}), 500

# PUT - ACTUALIZAR UN PEDIDO EXISTENTE
@pedido_bp.route('/pedido/<int:id>', methods=['PUT'])
def update_pedido(id):
    try:
        pedido = Pedido.query.get(id)
        if not pedido:
            return jsonify({'error': 'Pedido no encontrado'}), 404

        data = request.json

        # Atributos permitidos para la actualización
        updatable_fields = ['pedido_ropa', 'pedido_cantidad', 'observacion', 'fecha_servicio', 'idCliente', 'idMetodo_pago']
        
        # Actualiza solo los campos proporcionados en la solicitud
        for field in updatable_fields:
            if field in data:
                setattr(pedido, field, data[field])

        db.session.commit()

        # Obtener información detallada del Cliente y MetodoPago
        cliente = Cliente.query.get(pedido.idCliente)
        metodo_pago = MetodoPago.query.get(pedido.idMetodo_pago)

        response = pedido.serialize()
        response['cliente'] = cliente.serialize()
        response['metodo_pago'] = metodo_pago.serialize()

        return jsonify(response), 200
    except Exception as e:
        db.session.rollback()
        print("Error al actualizar el pedido:", str(e))
        return jsonify({'error': 'No se pudo actualizar el pedido'}), 500

#DELETE - ELIMINAR UN PEDIDO POR SU ID
@pedido_bp.route('/pedido/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    try:
        pedido = Pedido.query.get(id)
        if not pedido:
            return jsonify({'error': 'Pedido no encontrado'}), 404
        
        # Eliminar el pedido de la base de datos
        db.session.delete(pedido)
        db.session.commit()

        return jsonify({'message': 'Pedido eliminado correctamente'}), 200
    except Exception as e:
        print("Error al eliminar el pedido:", str(e))
        return jsonify({'error': 'No se pudo eliminar el pedido'}), 500