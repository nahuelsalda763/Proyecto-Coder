from django.urls import path
from mi_playground.views import formulario_empleados, formulario_proveedores, formulario_stock, index, busqueda_empleados, busqueda_proveedores, busqueda_stock


urlpatterns = [
    path('index/', index),
    path('empleados/', formulario_empleados),
    path('stock/', formulario_stock),
    path('proveedores/', formulario_proveedores )

]