from decimal import Decimal      # para garantir tipo correto do campo meta
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from usuario.forms import FormRegistroUsuario
from usuario.models import Usuario


def home(request):
    usuario = request.user
    saldo = Decimal(usuario.meta) - Decimal(usuario.valor)
    context = { "saldo" :  saldo}
    return render(request, "home.html", context)


