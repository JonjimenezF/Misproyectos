from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from alumnos.models import Producto
from django.contrib.admin.views.decorators import staff_member_required#restrijir pagina

# Create your views here.
def index(request):
    productos=Producto.objects.all() 
    context = {
        'productos' : productos
    } 
    return render(request, 'alumnos/index.html',context)#context ya lo contempla 


def Login(request):
    context = {} 
    return render(request, 'alumnos/Login.html')

def Registrarse(request):
    context = {} 
    return render(request, 'alumnos/Registrarse.html')

def ProductoList(request):
    productos=Producto.objects.all() 
    context = {
        'producto' : productos
    } 
    return render(request,'alumnos/index.html')

def ProductoById(request, id):
    try:
        producto = Producto.objects.get(id_prod=id)
        return render(request, 'alumnos/producto.html', {'producto': producto})
    except ObjectDoesNotExist:
        return render(request, 'producto_no_encontrado.html')

@staff_member_required   
def MantenedorProd(request):
    productos = Producto.objects.all()
    context ={
        'productos' : productos
    }
    return render(request,'administrador/ListaProductos.html',context)




# def Registrarse(request):
#     context={}
#     formulario =
#     if formulario.is_valid:
#         formulario.save()
#         context={'mensaje': "Usuario registrado"}