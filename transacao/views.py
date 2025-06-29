from django.shortcuts import render, redirect
from .forms import TransacaoForm
from django.contrib.auth.decorators import login_required
from .models import Transacao


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
            return redirect("transacao-lista")
    else:
        form = TransacaoForm(instance=transacao)
    return render(request, "transacao/transacao_form.html", {"form": form})

@login_required
def transacao_excluir(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk, usuario=request.user)
    if request.method == "DELETE":
        transacao.delete()
        return redirect("transacao-lista")
    # confirmação simples opcional
    return render(request, "transacao/confirm_delete.html", {"transacao": transacao})