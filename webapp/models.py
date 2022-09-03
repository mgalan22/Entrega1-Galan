from django.db import models



# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    content=models.TextField()
    #category=models.CharField(max_length=30) revisar como vincular con la otra clase

class Users(models.Model):
    mail=models.EmailField()
    name=models.CharField(max_length=50)
    #clave=models.CharField()   Revisar para cargar como password

class Post_categories(models.Model):
    name=models.CharField(max_length=30)
    post_qty=models.IntegerField()
