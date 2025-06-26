from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_criacao = models.DateTimeField(auto_now_add=True)
    meta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    @classmethod
    def criar_usuario(cls, nome, email, senha, meta):
        if len(senha) < 4:
            raise ValueError("Senha muito curta.")
        return cls(nome=nome, email=email, senha=senha, meta=meta)
    