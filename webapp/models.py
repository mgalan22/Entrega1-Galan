from ast import Pass
from pyexpat import model
from django.db import models



# Create your models here.
class publicaciones(models.Model):
    titulo=models.CharField(max_length=100)
    fecha=models.DateField()
    contenido=models.CharField(max_length=500)

class Usuarios(models.Model):
    mail=models.EmailField()
    nombre=models.CharField(max_length=50)
    #clave=models.CharField()   Revisar para cargar como password
