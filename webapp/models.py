from django.db import models



# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    content=models.CharField(max_length=500)

class Users(models.Model):
    mail=models.EmailField()
    name=models.CharField(max_length=50)
    #clave=models.CharField()   Revisar para cargar como password

class Post_categories(models.Model):
    name=models.CharField(max_length=30)
    cant_post=models.IntegerField()
