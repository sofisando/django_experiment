from mongoengine import Document, StringField, ListField, ReferenceField, EmailField, FloatField, IntField, BooleanField, DictField, DynamicField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField

class Categoria(Document):
    meta = {
        'collection': 'categoria_nueva'
    }
    nombre_categoria = StringField(required=True)
    descripcion = StringField()

class Producto(Document):
    meta = {
        'collection': 'productos_nueva',
        'allow_inheritance': True,
        'strict': False
    }
    nombre = StringField(required=True)
    descripcion = StringField()
    precio = FloatField(required=True)
    stock = IntField()
    imagenes = ListField(StringField())  
    detalle = DynamicField()
    categoria = ReferenceField(Categoria, required=False)  # Aquí corregimos el campo
    otros_datos = DynamicField()
