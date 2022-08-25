from django.shortcuts import render, redirect

#Formularios para inicio de sesion o crear usuarios.
from django.contrib.auth.forms import AuthenticationForm

#Formulario para autenticar 
from django.contrib.auth import login, authenticate
# Create your views here.

def inicio_sesion (request):
    
    if request.method == "GET":
        formulario = AuthenticationForm()
        return render(request, "autenticacion/login.html", {"form": formulario})
    else:
        formulario= AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            user = authenticate (username = data["username"], password = data ["password"]),
            
            if user is not None:
                login (request, user)
                return redirect ("index.html")