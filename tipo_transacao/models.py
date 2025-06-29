from django.db import models

# Create your models here.
class Tipo_Transacao(models.Model):
    descricao = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.descricao