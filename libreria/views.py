from django.http import JsonResponse
from django.views import View
from .models import Producto, Categoria  # Importamos ambos modelos
import json

class ProductoView(View):
    def get(self, request):
        productos = list(Producto.objects)
        data = [
            {
                "id": str(p.id),
                "nombre_producto": p.nombre,
                "precio_venta": p.precio,
                "descripcion": p.descripcion,
                "categoria_id": str(p.categoria.id) if p.categoria else None,
                "categoria_nombre": p.categoria.nombre if p.categoria else None
            }
            for p in productos
        ]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            body = json.loads(request.body)
            
            categoria = Categoria.objects(id=body["categoria"]).first()  # Buscar la categoría en la BD
            if not categoria:
                return JsonResponse({"error": "Categoría no encontrada"}, status=400)

            nuevo_producto = Producto(
                nombre=body["nombre"],
                precio=body["precio"],
                descripcion=body.get("descripcion", ""),
                categoria=categoria,  # Guardamos la referencia correcta
                detalle=body.get("detalle", {})
            )
            nuevo_producto.save()
            return JsonResponse({"message": "Producto creado", "id": str(nuevo_producto.id)}, status=201)

        except (json.JSONDecodeError, KeyError):
            return JsonResponse({"error": "Datos inválidos o faltantes"}, status=400)
