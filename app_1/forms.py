from tkinter.tix import MAX
from django import forms

class Curso_formulario(forms.Form):
    nombre: str = forms.CharField(max_length=50)
    comision: int = forms.IntegerField()

class Profesor_formulario(forms.Form):
    nombre: str = forms.CharField(max_length=50)
    apellido: str = forms.CharField(max_length=50)
    email: str = forms.EmailField()
    profesion: str =forms.CharField(max_length=50)