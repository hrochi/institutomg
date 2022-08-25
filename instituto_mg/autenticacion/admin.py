from django.contrib import admin
from autenticacion.views import inicio_sesion, usuarios_registrados

# Register your models here.

admin.site.register(usuarios_registrados),
admin.site.register(inicio_sesion)