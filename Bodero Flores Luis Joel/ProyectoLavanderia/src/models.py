from src.app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Cliente(db.Model, UserMixin):
    idCliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(75), nullable=False)
    cedula = db.Column(db.String(10), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    contraseña = db.Column(db.String(128), nullable=False)


    def serialize(self):
        return {
            'idCliente': self.idCliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'cedula': self.cedula,
            'correo': self.correo,
            'telefono': self.telefono
        }

    def __str__(self):
        return (
            f"Id: {self.idCliente}, "
            f"Nombre: {self.nombre}, "
            f"Apellido: {self.apellido}," 
            f"Cedula: {self.cedula}," 
            f"Correo: {self.correo}," 
            f"Telefono: {self.telefono}"
        )
    
    def get_id(self):
        return str(self.idCliente)
    
    def set_password(self, password):
        self.contraseña = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseña, password)

class MetodoPago(db.Model):
    idMetodo_pago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'idMetodo_pago': self.idMetodo_pago,
            'descripcion': self.descripcion
        }

    def __str__(self):
        return( 
            f"Id: {self.idMetodo_pago}, "
            f"Descripcion: {self.descripcion}"
        )

class TipoServicio(db.Model):
    idTipo_servicio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'idTipo_servicio': self.idTipo_servicio,
            'descripcion': self.descripcion
        }
    
    def __str__(self):
        return (
            f"Id: {self.idTipo_servicio}, "
            f"Descripcion: {self.descripcion}"
        )

class Pedido(db.Model):
    idPedido = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pedido_ropa = db.Column(db.String(50), nullable=False)
    pedido_cantidad = db.Column(db.String(10), nullable=False)
    observacion = db.Column(db.String(200), nullable=True)
    fecha_servicio = db.Column(db.Date, nullable=False)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.idCliente'), nullable=False)
    idMetodo_pago = db.Column(db.Integer, db.ForeignKey('metodo_pago.idMetodo_pago'), nullable=False)
    cliente = db.relationship('Cliente', backref='pedidos')
    metodo_pago = db.relationship('MetodoPago', backref='pedidos')

    def serialize(self):
        cliente = Cliente.query.get(self.idCliente)
        metodo_pago = MetodoPago.query.get(self.idMetodo_pago)
        servicios = [{
            'idPedido_servicio': servicio.idPedido_servicio,
            'cantidad': servicio.cantidad,
            'descripcion': servicio.descripcion,
            'tipo_servicio': {
                'idTipo_servicio': servicio.tipo_servicio.idTipo_servicio,
                'descripcion': servicio.tipo_servicio.descripcion
            }
        } for servicio in self.pedido_servicio]
        return {
            'idPedido': self.idPedido,
            'pedido_ropa': self.pedido_ropa,
            'pedido_cantidad': self.pedido_cantidad,
            'observacion': self.observacion,
            'fecha_servicio': self.fecha_servicio,
            'cliente': cliente.serialize() if cliente else None,
            'metodo_pago': metodo_pago.serialize() if metodo_pago else None,
            'servicios': servicios
        }

    def __str__(self):
        return (
            f"Id: {self.idPedido}, "
            f"Ropa: {self.pedido_ropa}, "
            f"Cantidad: {self.pedido_cantidad}, "
            f"Observacion: {self.observacion}, "
            f"Fecha de Servicio: {self.fecha_servicio}, "
            f"Id Cliente: {self.idCliente}, "
            f"Id Método de Pago: {self.idMetodo_pago}"
        )
    
class PedidoServicio(db.Model):
    idPedido_servicio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cantidad = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    idPedido = db.Column(db.Integer, db.ForeignKey('pedido.idPedido'), nullable=False)
    idTipo_servicio = db.Column(db.Integer, db.ForeignKey('tipo_servicio.idTipo_servicio'), nullable=False)
    
    pedido = db.relationship('Pedido', backref='pedido_servicio', lazy=True)
    tipo_servicio = db.relationship('TipoServicio', backref='pedido_servicio', lazy=True)

    def serialize(self):
        tipo_servicio = TipoServicio.query.get(self.idTipo_servicio)
        return {
            'idPedido_servicio': self.idPedido_servicio,
            'cantidad': self.cantidad,
            'descripcion': self.descripcion,
            'tipo_servicio': tipo_servicio.serialize() if tipo_servicio else None
        }

    def __str__(self):
        return (f"Id: {self.idPedido_servicio}, "
                f"Cantidad: {self.cantidad}, "
                f"Descripcion: {self.descripcion}, "
                f"Id Pedido: {self.idPedido}, "
                f"Id Tipo de Servicio: {self.idTipo_servicio}"
        )
