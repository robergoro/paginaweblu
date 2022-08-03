from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=250, null=False)

    def __str__(self) -> str:
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=True)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True )
    imagen = models.ImageField(upload_to='noticia', default='noticia/default.png')


    def __str__(self) -> str:
        return self.titulo
        