from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request,'index.html')

def Autores(request):
    return render (request, 'Autores.html')

def Noticias(request):
    return render (request, 'Noticias.html')