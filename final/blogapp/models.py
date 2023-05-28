from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo=models.CharField(max_length=100)
    resumen=models.CharField(max_length=150)
    texto=models.TextField()
    autor=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.titulo}'