from django.urls import path

from .views import *


urlpatterns = [

  path('', inicio, name="inicio"),
  path('index', index, name="index"),
  path('productos', productos, name="productos"),
  path('nuevosproductos', nuevosproductos, name="nuevosproductos"),
  path('nuevousuario', nuevousuario, name="nuevousuario"),
  path('formproductos', formproductos, name="formproductos"),
  path('formusuario', formusuario, name="formusuario"),
  path('modificarproducto/<id>', modificarproducto, name="modificarproducto"),
  path('eliminarproducto/<id>', eliminarproducto, name="eliminarproducto"),
  path('modificarusuario/<rut>', modificarusuario, name="modificarusuario"),
  path('eliminarusuario/<rut>', eliminarusuario, name="eliminarusuario"),
]