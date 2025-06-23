from django.db import models
from categoria.models import Categoria
# Create your models here.
class Gasto(models.Model):
    categoria = models.OneToOneField(Categoria)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    mes = models.PositiveSmallIntegerField(editable=False)
    ano = models.PositiveSmallIntegerField(editable=False)