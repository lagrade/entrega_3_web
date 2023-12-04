from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppWeb.models import Curso, Carrera, Profesor
from AppWeb.forms import Curso_form, Buscar_curso, Carrera_form, Buscar_carrera, Profesor_form
from django.views.generic import ListView


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
    contexto = {"cursos": cursos,
                "form": Buscar_curso()}

    return render(request, "AppWeb/cursos.html", contexto)


def buscar_curso(request):
    nombre = request.GET["curso"]
    cursos = Curso.objects.filter(nombre__icontains=nombre)
    contexto = {
        "cursos": cursos,
        "form": Buscar_curso()
    }
    return render(request, "AppWeb/cursos.html", contexto)


def agregar_carrera(request):
    if request.method == "POST":
        carrera_formu = Carrera_form(request.POST)
        if carrera_formu.is_valid():
            informacion = carrera_formu.cleaned_data

            carrera_nuevo = Carrera(nombre=informacion['carrera'], Modulos=informacion['modulos'])
            carrera_nuevo.save()
            return redirect(to="/app/carreras/")
    carrera_formulario = Carrera_form()

    contexto = {
        "form": carrera_formulario
    }
    return render(request, "AppWeb/agregar.html", contexto)


def mostrar_carreras(request):
    carreras = Carrera.objects.all()
    contexto = {"carreras": carreras,
                "form": Buscar_carrera()}

    return render(request, "AppWeb/carreras.html", contexto)


class CursoList(ListView):
    model = Curso
    template_name = "AppWeb/cursos1.html"


class CursoDetalle(ListView):
    model = Curso
    template_name = "AppWeb/curso_detalle.html"


def Leer_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "AppWeb/profesores.html", contexto)


def Profesores(request):
    if request.method == "POST":
        profesor_formu = Profesor_form(request.POST)
        print(profesor_formu)
        if profesor_formu.is_valid():
            informacion = profesor_formu.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], numero=informacion["numero"])
            profesor.save()
            return render(request, "AppWeb/agregar_profe.html")
    else:
        profesor_formu = Profesor_form()
    return render(request, "AppWeb/profesores.html")
