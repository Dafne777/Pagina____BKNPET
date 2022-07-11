from django.urls import path
from .views import acerca_de, home, contacto, acerca_de, registrar, pokebusca, recientes, \
    agregar_producto, modificar_producto, listar_productos, eliminar_producto,   \
    producto1,producto2,producto3,producto4,producto5,producto6,producto7,producto8,registro, \
    adopcion, agregar_mascota, listar_mascota, modificar_mascota, eliminar_mascota, mascota_collection, mascota_element


from rest_framework.urlpatterns import format_suffix_patterns
from app import views



urlpatterns = [
    # APP
    path('', home, name="home"),
    path('contacto/', contacto,name="contacto"),
    path('acerca_de/', acerca_de, name="acerca_de"),
    path('registrar/', registrar, name="registrar"),
    path('pokebusca/', pokebusca, name="pokebusca"),
    path('recientes/', recientes, name="recientes"),
    
    # CRUD
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/', listar_productos, name="listar_producto"),
    path('modificar-producto/<int:id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<int:id>/', eliminar_producto, name="eliminar_producto"),
    
    # REGISTRO FUNCIONAL
    path('registro/', registro, name="registro"),

    # API LOCAL
    path('api/', views.producto_collection, name='producto_collection'  ),
    path('api/<int:pk>/', views.producto_element, name= 'producto_element' ),
    
    # API MASCOTA
    path('api_mascota/', views.mascota_collection, name='mascota_collection'  ),
    path('api_mascota/<int:pk>/', views.mascota_element, name= 'mascota_element' ),
    
    # APP NUEVA
    path('adopcion/', adopcion, name="adopcion"),
    path('agregar_mascota/', agregar_mascota, name="agregar_mascota"),
    path('listar_mascota/', listar_mascota, name="listar_mascota"),
    path('modificar_mascota/<int:id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar_mascota/<int:id>/', eliminar_mascota, name="eliminar_mascota"),
    
    # PRODUCTOS
    path('producto1/', producto1, name="producto1"),
    path('producto2/', producto2, name="producto2"),
    path('producto3/', producto3, name="producto3"),
    path('producto4/', producto4, name="producto4"),
    path('producto5/', producto5, name="producto5"),
    path('producto6/', producto6, name="producto6"),
    path('producto7/', producto7, name="producto7"),
    path('producto8/', producto8, name="producto8"),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)