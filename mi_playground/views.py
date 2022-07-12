from django.shortcuts import render
from django.http import HttpResponse
from mi_playground.models import Empleados, Stock_Diesel, Proveedores
from mi_playground.forms import EmpleadosFormulario, StockBusquedaFormulario, StockFormulario, ProveedoresFormulario

def index(request):
    return render(request,"mi_playground/padre.html", {})

def formulario_empleados(request):

    if request.method == "POST":

        mi_formulario = EmpleadosFormulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            empleados = Empleados(nombre = datos["nombre"], edad = datos["edad"], nacionalidad = datos["nacionalidad"])
            empleados.save()
            

            return render(request, "mi_playground/stock_empleados.html", {"mensaje": "Empleado Registrado con exito! Bienvenido al equipo"})

    else:

        mi_formulario = EmpleadosFormulario()

        return render(request, "mi_playground/empleados_formulario.html", {"mi_formulario": mi_formulario})




def formulario_stock(request):
    
    if request.method == 'POST':

        mi_formulario = StockFormulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data
            stock = Stock_Diesel(repuesto = datos["repuesto"], marca = datos["marca"], codigo = datos["codigo"], cantidad = datos["cantidad"])
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

def formulario_busqueda(request):
    busqueda_formulario = StockBusquedaFormulario()

    if request.GET:
        resultado = Stock_Diesel.objects.filter(codigo=request.GET["criterio"]).all()


    else:
        resultado = []
        
    return render(request, "mi_playground/stock_busqueda.html", {"busqueda_formulario": busqueda_formulario, "resultado": resultado})   

# def formulario_busqueda(request):
#     busqueda_formulario = StockBusquedaFormulario()

#     if request.GET:
#         resultado = Stock_Diesel.objects.filter(codigo=busqueda_formulario["criterio"]).all()
#         # return render(request, "mi_playground/stock_busqueda.html", {"busqueda_formulario": busqueda_formulario, "stock": stock})
#     else:
#         resultado = []

#     return render(request, "mi_playground/stock_busqueda.html", {"busqueda_formulario": busqueda_formulario})


#prueba 2

# def buscar(request):
#     if request.GET["cod"]:

#         codigo = request.GET["cod"]
#         stock = Stock_Diesel.objects.filter(codigo__icontains=codigo)

#         return render(request, "mi_playground/busqueda_stock", { "codigo": codigo } )
#     else:
#         respuesta = "no ingresaste ningun dato"

#         return HttpResponse(respuesta)    
