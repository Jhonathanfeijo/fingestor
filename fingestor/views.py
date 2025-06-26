from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuario.forms import FormRegistroUsuario
from usuario.models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def logar(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = authenticate(email = email, senha = senha)
        if(usuario is not None):
            login(request, usuario)
            return redirect('home')
        else:
            print('vish')
            messages.error(request,'Crendencias inválidas')
            return redirect('login')
        
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        form = FormRegistroUsuario(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            meta = form.cleaned_data['meta']
            usuario = Usuario.criar_usuario(nome, email, senha, meta )
            usuario.save()
    else:
        form = FormRegistroUsuario()
    contexto = {'formulario' : form, }
    return render(request,'register.html', contexto)

