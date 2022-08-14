from django.urls import path
from institutos.views import *

urlpatterns = [
    path("", incio),
    path("estudiantes/",estudiantes),
    path("profesores/", profesores),
    path("cursos/", cursos),
    path("entregables", entregables)
]