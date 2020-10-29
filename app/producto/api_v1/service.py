from flask_restful import Resource, reqparse, request
from .schemas import ProductoSchema
from ...models import ProductoModel
from ...common.error_handling import ObjectNotFound, AppErrorBaseClass

#Clase modelo de un producto
class productoListResource(Resource):

    #inicializar el esquema de producto
    producto_schema = ProductoSchema()

    #Obtener todos los productos
    def get(self):
        producto = ProductoModel.get_all()
        resultado = self.producto_schema.dump(producto, many=True)
        return resultado

    #Guardar un producto
    def post(self):
        data = request.get_json()
        producto_dict = self.producto_schema.load(data)
        producto = ProductoModel(producto_dict['sku'], producto_dict['nombre'], producto_dict['descripcion'], producto_dict['precio'], producto_dict['cantidad'])
        producto.save()
        resultado = self.producto_schema.dump(producto)
        return resultado, 200
    
    #Modificar un producto
    def put(self, sku):
        data = request.get_json()
        producto_dict = self.producto_schema.load(data)

        #Buscar el producto a modicar
        producto = ProductoModel.query.filter_by(sku=sku).first()
        resultado = {}
        
        #Si el producto no se encuentra se lanza una excepción
        if producto:
            producto.sku = producto_dict['sku']
            producto.nombre = producto_dict['nombre']
            producto.descripcion = producto_dict['descripcion']
            producto.precio = producto_dict['precio']
            producto.cantidad = producto_dict['cantidad']
            ProductoModel.save(producto)
            resultado = {'msg': 'El producto con sku {0} fue modificado correctamente'.format(sku)}
            return resultado, 200
        else:
            raise ObjectNotFound('El producto con sku {0} no se encontro para su modificación'.format(sku))
        
    #Eliminar un producto
    def delete(self, sku):

        #Buscar el producto a eliminar
        producto = ProductoModel.query.filter_by(sku=sku).first()
        respuesta = {}

        #Si el producto no se encuentra se lanza una excepción
        if producto:
            ProductoModel.delete(producto)
            respuesta = {'mensaje': 'El producto con el sku {0} fue eliminado correctamente'.format(sku)}
            return respuesta, 200
        else:
            raise ObjectNotFound('El producto con sku {0} no se encontro para ser eliminado'.format(sku))

#Clase para consultar la cantidad total de un producto buscado por su SKU
class consultaCantidadProducto(Resource):
    
    def get(self, sku):

        #Buscar primero el producto
        producto = ProductoModel.query.filter_by(sku=sku).first()
        respuesta = {}

        #Si el producto no se encuentra se lanza una excepción
        if producto:
            if producto.cantidad <= 5:
                respuesta = {'Cantidad': producto.cantidad, "Observación": 'Cuentas con pocos productos, deberá ingresar mas al sistema'}
            else:
                respuesta = {'Cantidad': producto.cantidad}
            return respuesta, 200
        else:
            raise ObjectNotFound('El producto cuyo sku {0} no existe'.format(sku))
            

#Obtener la cantidad de dinero invertida en todos los productos
class obtenerTotalProducto(Resource):

    def get(self):
        producto_lista = ProductoModel.get_all()
        cantidad = 0
        for a in producto_lista:
            cantidad += a.precio*a.cantidad
        respuesta = {"mensaje": 'Total de dinero invertido es ${0} pesos'.format(cantidad)}
        return respuesta, 200 

        