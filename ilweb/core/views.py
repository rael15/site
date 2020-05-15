from django.shortcuts import render, redirect

# Create your views here.

def site(request):
    return render(request, "index.html")

def formulario(request):
    return render(request, 'formulario.html')