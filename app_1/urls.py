from django.urls import path
from app_1.views import *


urlpatterns = [
    path("curso/",curso),
    path("", inicio, name = "inicio"),
    path("cursos/", cursos, name = "cursos"),
    path("estudiantes/", estudiantes, name = "estudiantes"),
    path("profesores/", profesores, name = "profesores"),
    path("entregables/", entregables, name = "entregables"),
    path("curso_formulario/", curso_formulario, name = "curso_formulario"),
    path("profesor_formulario/", profesor_formulario, name = "profesor_formulario"),
    path("busqueda_comision/", busqueda_comision, name = "busqueda_comision"),
    path("buscar/", buscar, name = "buscar"),
]