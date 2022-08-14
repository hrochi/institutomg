from django.shortcuts import render
from django.http import HttpResponse
from institutos.models import Curso, Profesor, Estudiante, Entregable
from django.template import loader
from datetime import datetime

# Create your views here.

def incio(request):

    return render(request, "institutos/index.html")

def cursos(request):

    return HttpResponse('vista cursos')

def profesores(request):

    return HttpResponse('vista profesores')

def estudiantes(request):

    return HttpResponse('vista estudiantes')

def entregables(request):

    return HttpResponse('vista entregables')
