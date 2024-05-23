from flask import Blueprint, request, jsonify
from src.models import TipoServicio
from flask_jwt_extended import jwt_required

tiposervicio_bp = Blueprint('tipo_servicio', __name__)

# GET - OBTENER TODOS LOS TIPOS DE SERVICIO
@tiposervicio_bp.route('/tipo_servicio', methods=['GET'])
@jwt_required()
def get_tipos_servicio():
    try:
        tipos_servicio = TipoServicio.query.order_by(TipoServicio.idTipo_servicio.asc()).all()
        serialized_tipos_servicio = [tipo.serialize() for tipo in tipos_servicio]
        return jsonify(serialized_tipos_servicio), 200
    except Exception as e:
        print("Error al obtener los tipos de servicio:", str(e))
        return jsonify({'error': 'No se pudo obtener los tipos de servicio'}), 500

"""
# POST - CREAR UN NUEVO TIPO DE SERVICIO
@tiposervicio_bp.route('/tipo_servicio', methods=['POST'])
def create_tipo_servicio():
    try:
        data = request.json
        nuevo_tipo_servicio = TipoServicio(
            descripcion=data['descripcion']
        )
        db.session.add(nuevo_tipo_servicio)
        db.session.commit()
        return jsonify(nuevo_tipo_servicio.serialize()), 201
    except Exception as e:
        db.session.rollback()
        print("Error al crear el tipo de servicio:", str(e))
        return jsonify({'error': 'No se pudo crear el tipo de servicio'}), 500

# PUT - ACTUALIZAR UN TIPO DE SERVICIO EXISTENTE
@tiposervicio_bp.route('/tipo_servicio/<int:id>', methods=['PUT'])
def update_tipo_servicio(id):
    try:
        tipo_servicio = TipoServicio.query.get(id)
        if not tipo_servicio:
            return jsonify({'error': 'Tipo de servicio no encontrado'}), 404

        data = request.json
        updatable_fields = ['descripcion'] # Atributos permitidos para la actualización
        for field in updatable_fields:
            if field in data:
                setattr(tipo_servicio, field, data[field]) # Actualiza solo los campos proporcionados en la solicitud

        db.session.commit()
        return jsonify(tipo_servicio.serialize()), 200
    except Exception as e:
        db.session.rollback()
        print("Error al actualizar el tipo de servicio:", str(e))
        return jsonify({'error': 'No se pudo actualizar el tipo de servicio'}), 500

# DELETE - ELIMINAR UN TIPO DE SERVICIO POR SU ID
@tiposervicio_bp.route('/tipo_servicio/<int:id>', methods=['DELETE'])
def delete_tipo_servicio(id):
    try:
        tipo_servicio = TipoServicio.query.get(id)
        if tipo_servicio:
            db.session.delete(tipo_servicio)
            db.session.commit()
            return jsonify({'message': 'Tipo de servicio eliminado correctamente'}), 200
        else:
            return jsonify({'message': 'Tipo de servicio no encontrado'}), 404
    except Exception as e:
        db.session.rollback()
        print("Error al eliminar el tipo de servicio:", str(e))
        return jsonify({'error': 'No se pudo eliminar el tipo de servicio'}), 500

 """