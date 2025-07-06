from django.shortcuts import render

# Create your views here.
from decimal import Decimal      # para garantir tipo correto do campo meta
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormRegistroUsuario, PerfilForm
from .models import Usuario

def home(request):
    return render(request, "home.html")


def logar(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Com USERNAME_FIELD = "email", basta passar `username=email`
        usuario = authenticate(request, username=email, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect("home")
        else:
            messages.error(request, "Credenciais inválidas")
            return redirect("login")

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = FormRegistroUsuario(request.POST)

        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]
            meta = form.cleaned_data["meta"]  # já vem como Decimal pelo form

            # Usa o manager padrão do modelo
            Usuario.objects.create_user(
                email=email,
                password=senha,
                nome=nome,
                meta=Decimal(meta),  # só por garantia
            )

            messages.success(request, "Usuário criado com sucesso! Faça login.")
            return redirect("login")
    else:
        form = FormRegistroUsuario()

    contexto = {"formulario": form}
    return render(request, "register.html", contexto)

@login_required
def perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("perfil")   # recarrega em modo visualização
    else:
        form = PerfilForm(instance=request.user)

    return render(request, "usuario/perfil.html", {"form": form})

@login_required
def alterar_senha(request):
    if request.method == "POST":
        atual = request.POST.get("senha_atual")
        nova1 = request.POST.get("nova_senha1")
        nova2 = request.POST.get("nova_senha2")

        if not request.user.check_password(atual):
            messages.error(request, "Senha atual incorreta.")
        elif nova1 != nova2:
            messages.error(request, "As novas senhas não conferem.")
        else:
            request.user.set_password(nova1)
            request.user.save()
            update_session_auth_hash(request, request.user)  # mantém login
            messages.success(request, "Senha alterada com sucesso!")

    return redirect("perfil")            # volta para /perfil/

