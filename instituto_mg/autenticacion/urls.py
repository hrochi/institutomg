from django.urls import path
from autenticacion.views import inicio_sesion

urlpatterns = [
    path ("login/", inicio_sesion, name= "login"),
]
