from django.contrib import admin
from django.urls import path, include
from AppWeb.views import show, mostrar_cursos, agregar_curso_form

urlpatterns = [

    path('inicio/', show),
    path('cursos/', mostrar_cursos),
    path('agregar/', agregar_curso_form)

]