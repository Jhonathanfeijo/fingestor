from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.TextField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_criacao = models.DateTimeField(auto_now_add=True)
    meta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)