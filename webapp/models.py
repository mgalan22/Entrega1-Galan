from django.db import models



# Create your models here.
class Posts(models.Model):
    id=models.AutoField(primary_key=True)
    #active=models.BooleanField(default=True)
    title=models.CharField(max_length=100)
    date=models.DateField()
    content=models.TextField()
    #category=models.CharField(max_length=30) revisar como vincular con la otra clase
    
    def __str__(self): #con esto se arregla el formato que muestra el panel admin
        return f"Título: {self.title}, Fecha: {self.date}"

class Users(models.Model):
    mail=models.EmailField()
    name=models.CharField(max_length=50)
    #clave=models.CharField()   Revisar para cargar como password

class Post_categories(models.Model):
    name=models.CharField(max_length=30)
    post_qty=models.IntegerField()
