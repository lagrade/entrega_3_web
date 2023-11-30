from django import forms


class Curso_form(forms.Form):
    curso = forms.CharField()
    clases = forms.IntegerField()
