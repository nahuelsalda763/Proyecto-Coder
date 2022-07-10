from django.urls import path
from mi_playground.views import formulario_empleados, formulario_proveedores, formulario_stock, index, buscar


urlpatterns = [
    path('index/', index),
    path('empleados/', formulario_empleados),
    path('stock/', formulario_stock),
    path('proveedores/', formulario_proveedores ),
    path('busqueda_stock/',buscar)
]