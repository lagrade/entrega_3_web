from django.contrib import admin
from django.urls import path, include
from AppWeb.views import show, mostrar_cursos, agregar_curso_form, buscar_curso, mostrar_carreras, CursoList, \
    Leer_profesores, Profesores

urlpatterns = [

    path('inicio/', show),
    path('cursos/', mostrar_cursos),
    path('buscar/',buscar_curso),
    path('agregar/', agregar_curso_form),
    path('carreras/', mostrar_carreras),
    path('cursos-lista', CursoList.as_view(), name='listacursos'),
    path('leerprofesores', Leer_profesores, name="leerprofesores"),
    path("agregar-profesor", Profesores, name="agregar-profesor"),
]