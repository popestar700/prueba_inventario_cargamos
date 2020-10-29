from marshmallow import fields
from app.ext import ma

#Esquema para serializar un objeto perteneciente al modelo
class TiendaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    propietario = fields.String()
    direccion = fields.String()