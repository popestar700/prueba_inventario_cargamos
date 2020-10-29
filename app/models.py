from app.db import db, BaseModelMixin

#Modelo para la entidad de tienda
class Tienda(db.Model, BaseModelMixin):
    __tablename__ = 'inventario_tienda'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    propietario = db.Column(db.String)
    direccion = db.Column(db.String)

    def __init__(self, nombre, propietario, direccion):
        self.nombre = nombre
        self.propietario = propietario
        self.direccion = direccion

    def __repr__(self):
        return f'Nombre ({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'

#Modelo para la entidad de producto
class ProductoModel(db.Model, BaseModelMixin):
    __tablename__ = 'inventario_producto'
    
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer)
    nombre = db.Column(db.String)
    descripcion = db.Column(db.String)
    precio= db.Column(db.Float)
    cantidad = db.Column(db.Integer)

    def __init__(self, sku, nombre, descripcion, precio, cantidad):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f'Nombre ({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'