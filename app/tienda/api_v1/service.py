from flask_restful import Resource, reqparse, request
from .schemas import TiendaSchema
from ...models import Tienda

#Clase modelo para consultar y guardar informacion de una tienda
class TiendaListResource(Resource):

    #inicializar el esquema de tienda
    tienda_schema = TiendaSchema()

    #Obtener todas las tiendas registradas
    def get(self):
        tienda = Tienda.get_all()
        resultado = self.tienda_schema.dump(tienda, many=True)
        return resultado

    #Guardar la informacion de una nueva tienda
    def post(self):
        data = request.get_json()
        print(data)
        tienda_dict = self.tienda_schema.load(data)
        print(tienda_dict)
        tienda = Tienda(tienda_dict['nombre'], tienda_dict['propietario'], tienda_dict['direccion'])
        tienda.save()
        response = self.tienda_schema.dump(tienda)
        return response, 200