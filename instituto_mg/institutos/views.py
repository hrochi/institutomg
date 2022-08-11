from django.shortcuts import render
from django.http import HttpResponse
from institutos.models import Curso
from django.template import loader
from datetime import datetime

# Create your views here.

def lista_cursos(request):

    cursos = Curso.objects.all()

    lista_cursos_nombres = []

    for curso in cursos:
        lista_cursos_nombres.append(curso.nombre)

    return HttpResponse(lista_cursos_nombres)

def index(self):

    datos_contexto={"fecha_actual": datetime.now, "username": "gerson"}

    plantilla = loader.get_template("index.html")

    documento= plantilla.render(datos_contexto)

    return HttpResponse(documento)