from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, valor = 0, **extra_fields):
        if not email:
            raise ValueError("E-mail obrigatório")
        email = self.normalize_email(email)

        # Garante que "meta" foi enviado
        if "meta" not in extra_fields:
            raise ValueError("O campo 'meta' é obrigatório")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome  = models.CharField(max_length=255)

    # ---------- novo campo ----------
    meta  = models.DecimalField(
        max_digits=10,      # ex.: até 9 999 999,99
        decimal_places=2,
        null=False,
        blank=False
    )
    valor  = models.DecimalField(
        max_digits=10,      # ex.: até 9 999 999,99
        decimal_places=2,
        null=False,
        blank=False,
        default = 0
    )
    # ---------------------------------

    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ["nome", "meta"]    # torna obrigatório no createsuperuser
