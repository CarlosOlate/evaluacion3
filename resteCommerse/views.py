from django.shortcuts import render
from .serializers import ProveedorSerializer, GiroSerializer
from eCommerse.models import Proveedor, Giro

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Importamos para el login

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

# Restringimos accesos

from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt # sirve para que las solicitudes no sean rechazadas por no tener el token
@api_view(['GET', 'POST'])
#Restringimos que usuarios no logueados accedan
@permission_classes((IsAuthenticated,))
#Fin de eso de arriba
def listarProveedor(request):
    if request.method == 'GET':
        listado = Proveedor.objects.all() # select * from proveedor
        serializer = ProveedorSerializer(listado, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProveedorSerializer(data = request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

## Gestionar Proveedor
@csrf_exempt # filtro por token
@api_view(['GET', 'DELETE', 'PUT'])
#Restringimos que usuarios no logueados accedan
@permission_classes((IsAuthenticated,))
#Fin de eso de arriba
def gestionarProveedor(request, rut):
   
    try:
        objeto = Proveedor.objects.get(rut = rut)
    except Proveedor.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(ProveedorSerializer(objeto).data)
    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProveedorSerializer(objeto, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Giro y cosas...

@csrf_exempt # sirve para que las solicitudes no sean rechazadas por no tener el token
@api_view(['GET', 'POST'])
#Restringimos que usuarios no logueados accedan
@permission_classes((IsAuthenticated,))
#Fin de eso de arriba
def listarGiro(request):
    if request.method == 'GET':
        listado = Giro.objects.all() # select * from proveedor
        serializer = GiroSerializer(listado, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GiroSerializer(data = request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

## Gestionar Giro
@csrf_exempt # filtro por token
@api_view(['GET', 'DELETE', 'PUT'])
#Restringimos que usuarios no logueados accedan
@permission_classes((IsAuthenticated,))
#Fin de eso de arriba
def gestionarGiro(request, id):
   
    try:
        objeto = Giro.objects.get(id = id)
    except Giro.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(GiroSerializer(objeto).data)
    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = GiroSerializer(objeto, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Generamos el login

@csrf_exempt # filtro por token
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Buscamos en la base de patos
        try:
 
            usuario = User.objects.get(username = username)
        except User.DoesNotExist:
            return Response("Uuario no encontrado")

        # comprobar si la clave esta correcta
        esClaveValida = check_password(password, usuario.password)

        if not esClaveValida:
            return Response("Clave incorrecta")

        token, created = Token.objects.get_or_create(user= usuario)
        return Response(token.key) ## Token b8608395501ffcb378ffe796af34d11a7eeaccc2