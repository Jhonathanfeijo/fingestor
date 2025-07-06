from decimal import Decimal      # para garantir tipo correto do campo meta
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from usuario.forms import FormRegistroUsuario
from usuario.models import Usuario

from transacao.models import Transacao

from django.db.models import Sum, Aggregate

from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    user = request.user

    # Somatório de despesas e receitas
    despesas = (
        Transacao.objects
        .filter(usuario=user, tipo_transacao__descricao__iexact="Despesa")
        .aggregate(total=Sum("valor"))
        .get("total") or 0
    )

    receitas = (
        Transacao.objects
        .filter(usuario=user, tipo_transacao__descricao__iexact="Receita")
        .aggregate(total=Sum("valor"))
        .get("total") or 0
    )

    lucro = receitas - despesas

    return render(
        request,
        "home.html",
        {
            'total_receitas': receitas,
            "total_despesas": despesas,
            "lucro": lucro,
        },
    )