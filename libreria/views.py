from django.http import JsonResponse
from django.views import View
from .models import Producto  # Importamos el modelo desde la estructura modular
import json

class ProductoView(View):
    def get(self, request):
        productos = list(Producto.objects)  # Convertimos el QuerySet en una lista explícita
        data = [
            {
                "id": str(p.id),  # Convertimos ObjectId a string
                "nombre_producto": p.nombre,
                "precio_venta": p.precio,
                "descripcion": p.descripcion,
                "categoria": str(p.categoria.id) if p.categoria else None
            }
            for p in productos
        ]
        return JsonResponse(data, safe=False)


    def post(self, request):
        try:
            body = json.loads(request.body)
            nuevo_producto = Producto(
                nombre=body["nombre"],
                precio=body["precio"],
                descripcion=body.get("descripcion", ""),
                categoria=body.get("categoria"),  # Hay que verificar que el ID sea válido
                detalles=body.get("detalles", [])
            )
            nuevo_producto.save()
            return JsonResponse({"message": "Producto creado", "id": str(nuevo_producto.id)}, status=201)

        except (json.JSONDecodeError, KeyError):
            return JsonResponse({"error": "Datos inválidos o faltantes"}, status=400)
