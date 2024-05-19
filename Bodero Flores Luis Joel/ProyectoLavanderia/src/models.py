from src.app import db

class Cliente(db.Model):
    idCliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(75), nullable=False)
    cedula = db.Column(db.String(10), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(10), nullable=False)

    def __str__(self):
        return (
            f"Id: {self.idCliente}, "
            f"Nombre: {self.nombre}, "
            f"Apellido: {self.apellido}," 
            f"Cedula: {self.cedula}," 
            f"Correo: {self.correo}," 
            f"Telefono: {self.telefono}"
        )

class MetodoPago(db.Model):
    idMetodo_pago = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return( 
            f"Id: {self.idMetodo_pago}, "
            f"Descripcion: {self.descripcion}"
        )

class TipoServicio(db.Model):
    idTipo_servicio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return (
            f"Id: {self.idTipo_servicio}, "
            f"Descripcion: {self.descripcion}"
        )

class Pedido(db.Model):
    idPedido = db.Column(db.Integer, primary_key=True)
    pedido_ropa = db.Column(db.String(50), nullable=False)
    pedido_cantidad = db.Column(db.String(10), nullable=False)
    observacion = db.Column(db.String(200), nullable=True)
    fecha_servicio = db.Column(db.Date, nullable=False)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.idCliente'), nullable=False)
    idMetodo_pago = db.Column(db.Integer, db.ForeignKey('metodo_pago.idMetodo_pago'), nullable=False)

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
    idPedido_servicio = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    idPedido = db.Column(db.Integer, db.ForeignKey('pedido.idPedido'), nullable=False)
    idTipo_servicio = db.Column(db.Integer, db.ForeignKey('tipo_servicio.idTipo_servicio'), nullable=False)

    def __str__(self):
        return (f"Id: {self.idPedido_servicio}, "
                f"Cantidad: {self.cantidad}, "
                f"Descripcion: {self.descripcion}, "
                f"Id Pedido: {self.idPedido}, "
                f"Id Tipo de Servicio: {self.idTipo_servicio}"
        )
