from mongoengine import Document, StringField, ListField, ReferenceField, EmailField, FloatField, IntField, BooleanField

class Categoria(Document):
    nombre = StringField(required=True)
    descripcion = StringField()
    subcategorias = ListField(ReferenceField('Subcategoria'))  # Referencia a Subcategoria

class Subcategoria(Document):
    nombre = StringField(required=True)
    codigo = StringField(required=True)


from mongoengine import Document, StringField, FloatField, IntField, BooleanField, ReferenceField, ListField

class Categoria(Document):
    nombre = StringField(required=True)
    descripcion = StringField()

class Producto(Document):
    meta = {'collection': 'productos_nueva'}  # Nombre de la nueva colección en MongoDB
    nombre = StringField(required=True)
    descripcion = StringField()
    imagen = StringField()
    stock = IntField()
    categoria = ReferenceField(Categoria)
    clasificacion = StringField()
    marca = StringField()
    precio = FloatField(required=True)
    personalizable = BooleanField(default=False)
    detalles = ListField(StringField())


# class Producto(Document):
#     meta = {
#         'collection': 'producto',  # Asegúrate de que coincide con la colección en MongoDB
#         'allow_inheritance': True,  # Permite que existan subclases sin afectar la estructura
#         'strict': False  # Ignora los atributos desconocidos en MongoDB
#     }
#     nombre = StringField(required=True)
#     descripcion = StringField()
#     imagen = StringField()
#     stock = IntField()
#     categoria = ReferenceField(Categoria)
#     subcategoria = StringField()
#     clasificacion = StringField()
#     marca = StringField()
#     precio = FloatField(required=True)
#     personalizable = BooleanField(default=False)
#     detalles = ListField(StringField())  # Otros detalles como gramaje, tamaño, etc.



# class Cliente(Document):
#     nombre = StringField(required=True)
#     dni = StringField(required=True)
#     usuario = StringField(required=True, unique=True)
#     contraseña = StringField(required=True)
#     email = EmailField(required=True, unique=True)
#     metodos_pago = ListField(ReferenceField(MetodoPago))
#     carrito = ListField(StringField())  # Lista de IDs de productos en el carrito
#     historial_pedidos = ListField(StringField())  # Lista de IDs de pedidos
