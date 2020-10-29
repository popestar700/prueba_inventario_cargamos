from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Clase con los metodos de utilidad para el guardado de los objectos pertenecientes 
#a cada una de las entidaddes (Tienda, producto)

class BaseModelMixin:

    #Guardar y/o modificar un objecto
    def save(self):
        db.session.add(self)
        db.session.commit()

    #Eliminar un objecto
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #Obtener todos los registros de una entidad
    @classmethod
    def get_all(cls):
        return cls.query.all()

    #Obtener un objecto por su ID
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    #Obtener todos los objectos de una entidad, filtrado por un campo
    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()