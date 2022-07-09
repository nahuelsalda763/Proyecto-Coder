from unittest.util import _MAX_LENGTH
from urllib.request import AbstractDigestAuthHandler
from django.db import models
from django.forms import CharField

class Empleados(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=40)

class Stock_Diesel(models.Model):
    repuesto = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    codigo = models.CharField(max_length=40) 

class Proveedores(models.Model):
    respuesto_comprado = models.CharField(max_length=40)
    proveedor = models.CharField(max_length=40)


