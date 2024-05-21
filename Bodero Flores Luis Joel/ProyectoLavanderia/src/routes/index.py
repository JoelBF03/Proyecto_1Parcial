#src/routes/index.py
from .cliente_route import cliente_bp
from .metodo_pago_route import metodopago_bp
from .tipo_servicio_route import tiposervicio_bp
from .pedido_route import pedido_bp
from .pedido_servicio_route import pedidoservicio_bp

routes_blueprint = [
    cliente_bp,
    metodopago_bp,
    tiposervicio_bp,
    pedido_bp,
    pedidoservicio_bp
]