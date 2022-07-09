from xml.etree.ElementTree import fromstring
from django import forms

class EmpleadosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length=40)

class StockFormulario(forms.Form):
    repuesto = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    codigo = forms.CharField(max_length=40) 

class ProveedoresFormulario(forms.Form):
    respuesto_comprado = forms.CharField(max_length=40)
    proveedor = forms.CharField(max_length=40)

class EmpleadosBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

class StockBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

class ProveedoresBusquedaFormulario(forms.Form):
    criterio = forms.CharField

    