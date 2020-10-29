from marshmallow import fields
from app.ext import ma

#Esquema para serializar un objeto perteneciente al modelo
class ProductoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    sku = fields.Integer()
    nombre = fields.String()
    descripcion = fields.String()
    precio = fields.Float()
    cantidad = fields.Integer()