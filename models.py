from django.db import models

# Create your models here.
class Categoria(models.Model):
    id      = models.IntegerField(primary_key =True)
    nombre  = models.CharField(max_length=50)
    activo  = models.BooleanField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id          = models.IntegerField(primary_key =True)
    codigoBarra = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    precioCosto = models.IntegerField()
    precioVenta = models.IntegerField()
    marca       = models.CharField(max_length=50)
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:  
        db_table = "producto"  
    def __str__(self):
        return self.descripcion + " " + self.marca



class Pais(models.Model):
    id      = models.IntegerField(primary_key =True)
    nombre  = models.CharField(max_length=100)
    activo  = models.BooleanField()

    def __str__(self):
        return self.nombre


class NivelEducacional(models.Model):
    id      = models.IntegerField(primary_key =True)
    nombre  = models.CharField(max_length=50)
    activo  = models.BooleanField()

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    rut      = models.IntegerField(primary_key =True)
    nombre   = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo   = models.EmailField(max_length=50)
    fechaNac = models.CharField(max_length=50)
    telefono = models.IntegerField()
    pais     = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nvledu   = models.ForeignKey(NivelEducacional, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre + " " + self.apellido