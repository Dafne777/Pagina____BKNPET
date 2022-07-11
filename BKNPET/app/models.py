from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre
    


# -----------------------------------------------------------------------------------
#                               APP NUEVA
class Mascota(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    raza = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10, null=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="mascotas", null=True)
    
    
    def __str__(self):
        return self.raza
