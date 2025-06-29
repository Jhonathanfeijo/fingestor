from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.categoria_name
        