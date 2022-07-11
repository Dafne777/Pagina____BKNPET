from unicodedata import category
from django.contrib import admin
from .models import Categoria, Producto, Mascota

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Mascota)