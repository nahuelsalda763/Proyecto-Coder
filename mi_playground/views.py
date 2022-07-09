from django.shortcuts import render
from django.http import HttpResponse
from mi_playground.models import Empleados, Stock_Diesel, Proveedores
from mi_playground.forms import EmpleadosBusquedaFormulario, EmpleadosFormulario, StockBusquedaFormulario, StockFormulario, ProveedoresFormulario

def index(request):
    return render(request,"mi_playground/index.html", {})

def formulario_empleados(request):

    if request.method == "POST":
        
        mi_formulario = EmpleadosFormulario(request.POST)

        if mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data
            empleados = Empleados(nombre = datos["nombre"], edad = datos["edad"], nacionalidad = datos["nacionalidad"])
            empleados.save()

            return render(request, "mi_playground/empleados_formulario.html", {"mensaje": "Empleado agregado con exito! Bienvenido al equipo"})

    else:

        mi_formulario = EmpleadosFormulario()

        return render(request, "mi_playground/empleados_formulario.html", {"mi_formulario": mi_formulario})



def formulario_stock(request):
    
    if request.method == 'POST':

        mi_formulario = StockFormulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:

            datos = mi_formulario.cleaned_data
            stock = Stock_Diesel(repuesto = datos["repuesto"], marca = datos["marca"], codigo = datos["codigo"])
            stock.save()

            return render(request, "mi_playground/stock_formulario.html", {"mensaje": "Mercaderia ingresada con exito!"})
    else:
        mi_formulario = StockFormulario()
        return render(request, "mi_playground/stock_formulario.html", {"mi_formulario": mi_formulario})



def formulario_proveedores(request):

    if request.method == "POST":

        mi_formulario = ProveedoresFormulario(request.POST)

        if mi_formulario.is_valid:
            
            datos = mi_formulario.cleaned_data
            proveedores = Proveedores(repuesto_comprado = datos["datos_comprados"], proveedor = datos["proveedor"])
            proveedores.save()

            return render(request, "mi_playground/proveedores_formulario.html", {"mensaje": "Datos guardados correctamente!"})

    else:
        mi_formulario = ProveedoresFormulario()
        return render(request, "mi_playground/proveedores_formulario.html", {"mi_formulario": mi_formulario})



def busqueda_empleados(request):
    
    busqueda_formulario = EmpleadosBusquedaFormulario()

    if request.GET:
        empleados = Empleados.objects.filter(nombre = busqueda_formulario["criterio"]).all()
        return render(request, "mi_playground/empleados_busqueda.html", {"busqueda_formulario": busqueda_formulario, "empleados": empleados})

    return render(request, "mi_playground/empleados_busqueda.html", {"busqueda_formulario": busqueda_formulario})



def busqueda_stock(request):
    busqueda_formulario = StockBusquedaFormulario()

    if request.GET:
        stock = Stock_Diesel.objects.filter(codigo = busqueda_formulario["criterio"]).all()
        return render(request, "mi_playground/stock_busqueda.html", {"busqueda_formulario": busqueda_formulario, "stock": stock})

    return render(request, "mi_playground/stock_busqueda.html", {"busqueda_formulario": busqueda_formulario})



def busqueda_proveedores(request):
    busqueda_formulario = ProveedoresFormulario

    if request.GET:

        proveedor = Proveedores.objects.filter(proveedor = busqueda_formulario["criterio"]).all()
        return render(request, "mi_playground/proveedor_busqueda.html", {"busqueda_formulario": busqueda_formulario, "proveedor": proveedor })

    return render(request, "mi_playground/proveedor_busqueda.html", {"busqueda_formulario": busqueda_formulario})

    

# Create your views here.
