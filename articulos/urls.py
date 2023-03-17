from django.urls import path 
from .views import listar_articulos, crear_articulo, eliminar_articulo, actualizar_articulo, UpdateArticulo

urlpatterns = [
    path('', listar_articulos),
    path('new/', crear_articulo, name='nuevo_articulo'),
    path('eliminar/<int:articulo_id>/', eliminar_articulo, name='borrar_articulo'),
    path('actualizar/<int:articulo_id>/', actualizar_articulo, name='editar_articulo'),
    path('update/<int:articulo_id>/', UpdateArticulo, name='update_articulo')
     
] 