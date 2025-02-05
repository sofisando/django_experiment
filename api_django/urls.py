from django.urls import path
from libreria.views import ProductoView

urlpatterns = [
   # path('admin/', admin.site.urls), # Django admin predeterminado para SQL
    path('productos/', ProductoView.as_view(), name='productos')
]
