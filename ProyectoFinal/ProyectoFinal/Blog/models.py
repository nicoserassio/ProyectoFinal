from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f'Usuario: {self.usuario} '

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    publicado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Titulo: {self.titulo} - Subtitulo: {self.subtitulo} - Autor: {self.autor} - Creado: {self.publicado}'


