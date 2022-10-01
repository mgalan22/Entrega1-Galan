from django.db import models


class Post(models.Model):
    id=models.AutoField(primary_key=True)
    #active=models.BooleanField(default=True)
    title=models.CharField(max_length=100)
    date=models.DateField()
    content=models.TextField()
    
    
    def __str__(self): #con esto se arregla el formato que muestra el panel admin
        return f"Título: {self.title}, Fecha: {self.date}"


class Post_category(models.Model):
    name=models.CharField(max_length=30)
    post_qty=models.IntegerField()


