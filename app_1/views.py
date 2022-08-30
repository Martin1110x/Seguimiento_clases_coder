from django.http import  HttpResponse
from .models import Curso
from django.shortcuts import render
# Create your views here.

def curso(request):
    curso_1: object = Curso(nombre = "C#", comision = 25441)
    curso_2: object = Curso(Nombre = "Python", comision = 31105)
    curso_3: object = Curso(nombre = "html y css", comision = 14367)
    curso_1.save()
    curso_2.save()
    curso_3.save()
    texto = f"Cursos creados."
    return HttpResponse(texto)

def inicio(request):
    return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/inicio.html")

def cursos(request):
    return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/cursos.html")

def profesores(request):
    return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/profesores.html")

def estudiantes(request):
    return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/estudiantes.html")

def entregables(request):
    return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/entregables.html")