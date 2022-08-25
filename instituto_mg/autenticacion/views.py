from django.shortcuts import render, redirect

#Formularios para inicio de sesion o crear usuarios.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#Formulario para autenticar 
from django.contrib.auth import login, authenticate
# Create your views here.

def inicio_sesion (request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            user = authenticate (username = data ["username"], password = data ["password"]),
            
            if user is not None:
                login (request, user)
                return render (request, "autenticacion/login.html", {"mensaje": f"Bienvenido {usuario}"})
        
            else:
                return render (request, "autenticacion/login.html", {"mensaje": "Datos incorrectos, vuelva a intentar."})
                formulario= AuthenticationForm(request, data=request.POST)
        
        else:
            
            return render (request, "autenticacion/login.html", {"mensaje": "Formulario erroneo"})
                
    formulario = AuthenticationForm() 
    return render (request, "autenticacion/login.html", {"form": formulario})
    
    
def usuarios_registrados(request):
    if request.method == "GET":
        formulario = UserCreationForm()
        return render (request, "autenticacion/registrados.html", {"form": formulario})
    
    else:
        formulario = UserCreationForm(request.POST) 
        
        if formulario.is_valid():
            formulario.save()
    
    return redirect ("institutos/index.html", {"mensaje": "Usuario Creado"})