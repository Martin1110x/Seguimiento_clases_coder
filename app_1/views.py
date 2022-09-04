from django.http import  HttpResponse
from .models import Curso, Profesor
from django.shortcuts import render
from app_1.forms import Curso_formulario, Profesor_formulario
# Create your views here.

def curso(request):
    curso_1: object = Curso(nombre = "C#", comision = 25441)
    curso_2: object = Curso(nombre = "Python", comision = 31105)
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

def curso_formulario(request):
    if request.method == "POST":
        formulario = Curso_formulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            curso = Curso(nombre = informacion["nombre"], comision = informacion["comision"])
            curso.save()
            return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/inicio.html")
    else:
        formulario = Curso_formulario()
    return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/curso_formulario.html", {"formulario": formulario})

def profesor_formulario(request):
    if request.method == "POST":
        formulario = Profesor_formulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesor = Profesor(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"], profesion = informacion["profesion"])
            profesor.save()
            return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/inicio.html")
    else:
        formulario = Profesor_formulario()
    return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/profesor_formulario.html", {"formulario": formulario})

def busqueda_comision(request):
    return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/busqueda_comision.html")

def buscar(request):
    if request.GET["comision"]:
        comision: int = request.GET["comision"]
        cursos = Curso.objects.filter(comision = comision)
        return render(request, "C:/Users/MARTIN/Desktop/carpeta_generica/Proyecto_ejemplo_clases_coder/proyecto_1_ejemplo/app_1/templates/resultados_busqueda.html", {"cursos": cursos, "comision": comision})
    else:
        texto: str = "No enviaste datos."
    return HttpResponse(texto)