from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def home_layout(request):
    return render(request,'layout.html')
