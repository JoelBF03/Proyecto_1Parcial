from flask import Blueprint, request, jsonify
from src.models import Pedido, Cliente, MetodoPago, TipoServicio, PedidoServicio
from src.app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

pedido_bp = Blueprint('pedido', __name__)

#GET - OBTENER TODOS LOS PEDIDOS DEL CLIENTE AUTENTICADO
@pedido_bp.route('/pedido', methods=['GET'])
@jwt_required()
def get_pedidos():
    try:
        cliente_id = get_jwt_identity()
        pedidos = Pedido.query.filter_by(idCliente = cliente_id).order_by(Pedido.idPedido.asc()).all()
        serialized_pedidos = [pedido.serialize() for pedido in pedidos]
        return jsonify(serialized_pedidos), 200
    except Exception as e:
        print("Error al obtener los pedidos:", str(e))
        return jsonify({'error': 'No se pudo obtener los pedidos'}), 500

# GET - OBTENER UN PEDIDO POR SU ID (DEL CLIENTE AUTENTICADO)
@pedido_bp.route('/pedido/<int:idPedido>', methods=['GET'])
@jwt_required()
def get_pedido_by_id(idPedido):
    try:
        cliente_id = get_jwt_identity()
        pedido = Pedido.query.filter_by(idPedido = idPedido, idCliente = cliente_id).first()
        if not pedido:
            return jsonify({'error': 'Pedido no encontrado o no autorizado'}), 404
        
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
@jwt_required()
def create_pedido():
    try:
        cliente_id = get_jwt_identity()
        data = request.json

        # Crear nuevo pedido con los datos proporcionados
        nuevo_pedido = Pedido(
            pedido_ropa=data.get('pedido_ropa'),
            pedido_cantidad=data.get('pedido_cantidad'),
            observacion=data.get('observacion'),
            fecha_servicio=data.get('fecha_servicio'),
            idCliente=cliente_id,
            idMetodo_pago=data.get('idMetodo_pago')
        )
        
        # Crear detalles del servicio para el pedido
        for servicio in data.get('servicios', []):
            tipo_servicio_id = servicio.get('tipo_servicio_id')
            cantidad = servicio.get('cantidad')
            descripcion = servicio.get('descripcion')
            
            # Verificar si el tipo de servicio existe, si no, crearlo
            tipo_servicio = TipoServicio.query.get(tipo_servicio_id)
            if not tipo_servicio:
                tipo_servicio = TipoServicio(idTipo_servicio=tipo_servicio_id, descripcion='Nuevo Tipo de Servicio')
                db.session.add(tipo_servicio)
            
            # Crear detalle del servicio para el pedido
            nuevo_detalle = PedidoServicio(
                cantidad=cantidad,
                descripcion=descripcion,
                pedido=nuevo_pedido,
                tipo_servicio=tipo_servicio
            )
            db.session.add(nuevo_detalle)

        db.session.add(nuevo_pedido)
        db.session.commit()

        return jsonify(nuevo_pedido.serialize()), 201
    except Exception as e:
        db.session.rollback()
        print("Error al crear el pedido:", str(e))
        return jsonify({'error': 'No se pudo crear el pedido'}), 500

# PUT - ACTUALIZAR UN PEDIDO EXISTENTE
@pedido_bp.route('/pedido/<int:idPedido>', methods=['PUT'])
@jwt_required()
def update_pedido(idPedido):
    try:
        cliente_id = get_jwt_identity()
        pedido = Pedido.query.filter_by(idPedido = idPedido, idCliente = cliente_id).first()
        if not pedido:
            return jsonify({'error': 'Pedido no encontrado'}), 404

        data = request.json

        # Atributos permitidos para la actualización
        updatable_fields = ['pedido_ropa', 'pedido_cantidad', 'observacion', 'fecha_servicio', 'idMetodo_pago']
        
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

""" 
# Solo los administradores pueden borrar pedidos

#DELETE - ELIMINAR UN PEDIDO POR SU ID
@pedido_bp.route('/pedido/<int:idPedido>', methods=['DELETE'])
@jwt_required()
def delete_pedido(idPedido):
    try:
        cliente_id = get_jwt_identity()
        pedido = Pedido.query.filter_by(idPedido = idPedido, idCliente = cliente_id).first()
        if not pedido:
            return jsonify({'error': 'Pedido no encontrado o autorizado'}), 404
        
        # Eliminar el pedido de la base de datos
        db.session.delete(pedido)
        db.session.commit()

        return jsonify({'message': 'Pedido eliminado correctamente'}), 200
    except Exception as e:
        print("Error al eliminar el pedido:", str(e))
        return jsonify({'error': 'No se pudo eliminar el pedido'}), 500

 """