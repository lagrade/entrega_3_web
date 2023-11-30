from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    clases = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre}, Clases: {self.clases}"


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    modulos = models.IntegerField()

    def __str__(self):
        return f"Carrera: {self.nombre}, Modulos: {self.modulos}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return f"Profesor: {self.nombre}, Legajo: {self.numero}"
