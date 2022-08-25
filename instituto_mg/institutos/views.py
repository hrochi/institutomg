from django.shortcuts import render
from django.http import HttpResponse
from institutos.models import Curso, Profesor, Estudiante, Entregable
from django.template import loader
from datetime import datetime

# Create your views here.

def inicio(request):

    return render(request, "institutos/index.html")

def comentarios(request):

    return render(request, "institutos/comentarios.html")

def cursos(request):

    return render(request, "institutos/cursos.html")

def campus(request):

    return render(request, "institutos/campus.html")

def usuario(request):

    return render(request, "institutos/usuario.html")

def fisica(request):

    return render(request, "institutos/fisica.html")

def quimica(request):

    return render(request, "institutos/quimica.html")

def matematica(request):

    return render(request, "institutos/matematica.html")

def login(request):

    return render(request, "institutos/iniciar_sesion.html")
