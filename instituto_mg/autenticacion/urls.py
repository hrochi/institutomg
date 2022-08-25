from django.urls import path
from autenticacion.views import inicio_sesion, usuarios_registrados


urlpatterns = [
    path ("login/", inicio_sesion, name= "login"),
    path ("registrar/", usuarios_registrados, name= "registrar")
]
