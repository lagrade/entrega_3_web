from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppWeb.models import Curso, Carrera, Profesor
from AppWeb.forms import Curso_form


def show(request):
    curso = Curso.objects.all()
    contexto = {}
    return render(request, "index.html", contexto)


def agregar_curso_form(request):
    if request.method == "POST":
        curso_formu = Curso_form(request.POST)
        if curso_formu.is_valid():
            informacion = curso_formu.cleaned_data

            curso_nuevo = Curso(nombre=informacion['curso'], clases=informacion['clases'])
            curso_nuevo.save()
            return redirect(to="/app/cursos/")
    curso_formulario = Curso_form()

    contexto = {
        "form": curso_formulario
    }
    return render(request, "AppWeb/agregar.html", contexto)


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos, }

    return render(request, "AppWeb/cursos.html", contexto)
