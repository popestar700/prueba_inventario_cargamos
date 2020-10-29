from flask import request, Blueprint
from flask_restful import Api, Resource
from .service import productoListResource, consultaCantidadProducto, obtenerTotalProducto

producto_v1_bp = Blueprint('producto_v1_bp', __name__)

api = Api(producto_v1_bp)

#Registro de los endpoints para su consumo
api.add_resource(productoListResource, '/api/v1/producto/', '/api/v1/producto/<int:sku>', endpoint='producto_list_resource')
api.add_resource(consultaCantidadProducto, '/api/v1/producto/consultarCantidadProducto/<int:sku>/', endpoint="cantidad_producto")
api.add_resource(obtenerTotalProducto, '/api/v1/producto/obtenerTotalProducto/', endpoint="total_producto")
