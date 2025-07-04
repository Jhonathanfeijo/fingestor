from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransacaoForm
from django.contrib.auth.decorators import login_required
from .models import Transacao
from django.db.models.functions import TruncMonth
from django.db.models import Sum

def transacao_nova(request):
    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.usuario = request.user  # associa ao usuário logado
            transacao.save()
            return redirect("home")
    else:
        form = TransacaoForm()
    return render(request, "transacao/transacao_form.html", {"form": form})

@login_required
def transacao_lista(request):
    transacoes = (
        Transacao.objects.filter(usuario=request.user)
        .select_related("categoria", "tipo_transacao")
        .order_by("-data")        # mais recente primeiro
    )
    return render(request, "transacao/transacao.html", {"transacoes": transacoes})

@login_required
def transacao_editar(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk, usuario=request.user)

    if request.method == "POST":
        form = TransacaoForm(request.POST, instance=transacao)
        if form.is_valid():
            form.save()
            return redirect("transacao_form")
    else:
        form = TransacaoForm(instance=transacao)

    # passando flag para o template mudar título/botão
    return render(
        request,
        "transacao/transacao_form.html",
        {"form": form, "is_edit": True, "obj": transacao},
    )

@login_required
def transacao_excluir(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk, usuario=request.user)
    if request.method == "POST":
        transacao.delete()
        return redirect("transacoes")
    # confirmação simples opcional
    return render(request, "transacao/confirm_delete.html", {"transacao": transacao})

@login_required
def relatorios(request):
    user = request.user

    # 1) Relatório mensal – soma de despesas por mês (últimos 12)
    mensal = (
        Transacao.objects
        .filter(usuario=user, tipo_transacao__descricao__iexact="Despesa")
        .annotate(mes=TruncMonth("data"))
        .values("mes")
        .annotate(total=Sum("valor"))
        .order_by("-mes")            # ← mês mais novo primeiro
    )

    maiores = (
        Transacao.objects
        .filter(usuario=user, tipo_transacao__descricao__iexact="Despesa")
        .values("categoria__categoria_name")           # agrupa pela descrição da categoria
        .annotate(total=Sum("valor"))             # soma dos valores
        .order_by("-total")[:10]                  # do maior para o menor
    )

    return render(
        request,
        "transacao/relatorios.html",
        {"mensal": mensal, "maiores": maiores},
    )