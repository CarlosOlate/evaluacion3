from django.urls import path
from .views import *

urlpatterns = [
    path('listarProveedor', listarProveedor, name="listarProveedor"),
    ## Colocamos el gestionar
    path('gestionarProveedor/<rut>', gestionarProveedor, name="gestionarProveedor"),
    ## Giro
    path('listarGiro', listarGiro, name="listarGiro"),
    path('gestionarGiro/<id>', gestionarGiro, name="gestionarGiro"),
    ## Agregamos el login
    path('login', login, name="login"),

]