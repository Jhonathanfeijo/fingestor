from django.http import HttpResponse
from django.shortcuts import render
from usuario.forms import FormRegistroUsuario
from usuario.models import Usuario

def home(request):
    return render(request,'home.html')

def login(request):
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

