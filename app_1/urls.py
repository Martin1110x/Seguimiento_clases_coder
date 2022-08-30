from django.urls import path
from app_1.views import *


urlpatterns = [
    path("curso/",curso),
    path("", inicio, name = "inicio"),
    path("cursos/", cursos, name = "cursos"),
    path("estudiantes/", estudiantes, name = "estudiantes"),
    path("profesores/", profesores, name = "profesores"),
    path("entregables/", entregables, name = "entregables"),

]