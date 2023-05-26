from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.
class Libros(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagen/', null=True,verbose_name='Imagen')
    descripcion = models.TextField(verbose_name='Descripción',null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):   
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre