from django import forms



class Comentarios(forms.Form):

    #Variables de comentarios
    Nombre = forms.CharField()
    Comentario = forms.CharField()