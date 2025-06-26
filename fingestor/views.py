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
            print(form)
            print(request.body)
            nome = form.changed_data['id_nome']
            email = form.changed_data['id_email']
            senha = form.changed_data['id_senha']
            meta = form.changed_data['id_meta']
            usuario = Usuario.criar_usuario(nome, email, senha, meta )
            usuario.save()
    
    form = FormRegistroUsuario()
    contexto = {'formulario' : form, }
    return render(request,'register.html', contexto)

