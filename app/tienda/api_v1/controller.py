from flask import request, Blueprint
from flask_restful import Api, Resource
from .service import TiendaListResource

tienda_v1_bp = Blueprint('tienda_v1_bp', __name__)

api = Api(tienda_v1_bp)

#Registro de los endpoints para su consumo
api.add_resource(TiendaListResource, '/api/v1/tienda/', endpoint='tienda_list_resource')
