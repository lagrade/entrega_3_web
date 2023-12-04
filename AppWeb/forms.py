from django import forms


class Curso_form(forms.Form):
    curso = forms.CharField()
    clases = forms.IntegerField()


class Carrera_form(forms.Form):
    carrera = forms.CharField()
    modulos = forms.IntegerField


class Buscar_curso(forms.Form):
    curso = forms.CharField()


class Buscar_carrera(forms.Form):
    carrera = forms.CharField()


class Profesor_form(forms.Form):
    nombre = forms.CharField(max_length=50)
    numero = forms.IntegerField()
