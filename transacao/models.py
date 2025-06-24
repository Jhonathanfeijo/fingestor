from django.db import models
from tipo_transacao.models import Tipo_Transacao
from categoria.models import Categoria
from usuario.models import Usuario

# Create your models here.
class Transacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transacoes')
    tipo_transacao = models.ForeignKey(Tipo_Transacao, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    