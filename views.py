from django.shortcuts import render, redirect
from .models import *
from .forms import *

def inicio(request):
    return render(request, 'plantillaBase.html')

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')


def nuevosproductos(request):
    listado = Producto.objects.all()
    contexto = {'listado' : listado}
    return render(request, 'nuevosproductos.html', contexto)

def nuevousuario(request):
    listado = Usuario.objects.all()
    contexto = {'listado' : listado}
    return render(request, 'nuevousuario.html', contexto)


def formproductos(request):
    contexto = { 'form' : ProductoForm }
    if request.method == 'POST':
        producto = ProductoForm(request.POST)
        
        producto.save()
    return render(request, 'formproductos.html', contexto)


def formusuario(request):
    contexto = { 'form' : UsuarioForm }
    if request.method == 'POST':
        usuario = UsuarioForm(request.POST)
        usuario.save()
    return render(request, 'formusuario.html', contexto)



def modificarproducto(request, id):
    producto = Producto.objects.get(id = id)

    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance=producto)
        formulario.save()

    contexto = { 'form' : ProductoForm(instance=producto) }
    return render(request, 'modificarproducto.html', contexto)


def eliminarproducto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect(to="productos")

 

def modificarusuario(request, rut):
    usuario = Usuario.objects.get(rut = rut)

    if request.method == 'POST':
        formulario = UsuarioForm(data = request.POST, instance=usuario)
        formulario.save()

    contexto = { 'form' : UsuarioForm(instance=usuario) }
    return render(request, 'modificarusuario.html', contexto)

def eliminarusuario(request, rut):
    usuario = Usuario.objects.get(rut = rut)
    usuario.delete()
    return redirect(to="nuevousuario")
