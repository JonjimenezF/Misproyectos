from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from alumnos.forms import AddProductoForm
from alumnos.models import Producto
from django.contrib.admin.views.decorators import staff_member_required#restrijir pagina
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as djlogin
# Create your views here.
def index(request):
    productos=Producto.objects.all() 
    context = {
        'productos' : productos
    } 
    return render(request, 'alumnos/index.html',context)#context ya lo contempla 


def login(request):
    context = {} 
    
    return render(request, '../templates/registration/login.html')



def registrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Crear un nuevo usuario
        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Te has registrado correctamente")
            user = authenticate(username=username, password=password)
            djlogin(request, user)
            return redirect('index')
        
        else:
            messages.success(request, "Contraseña no coinciden")
            return render(request, '../templates/registration/registrar.html')
            
        # Redireccionar a una página de éxito o hacer cualquier otra acción requerida
        
    return render(request, '../templates/registration/registrar.html')

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

@staff_member_required   
def AgregarProducto(request):
    if Producto.objects.all().count()==0:
        idProducto=1
    else:
        idProducto=Producto.objects.latest("id_prod")
        idProducto=idProducto.id_prod+1
        print(idProducto)
    datos = {
        'idProducto':idProducto,
        'form': AddProductoForm(),
    }
    if request.method == "POST":
        print('hola')
        producto = AddProductoForm(request.POST, request.FILES)
        print(producto)
        if producto.is_valid():
            producto.id_prod = request.POST.get("id_id_prod")
            producto.nombre_prod = request.POST.get("id_nombre_prod")
            producto.precio_prod = request.POST.get("id_precio_prod")
            producto.img_prod = request.FILES.get("id_img_prod")
            print('medio')
            producto.save()
            print('chao')
            messages.success(request, "Producto agregado correctamente")
            return redirect(to="Mantenedor")
    return render(request, 'administrador/agregarProducto.html', datos)

@staff_member_required  
def EliminarProducto(request, id):
    producto = Producto.objects.get(id_prod=id)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Producto Eliminado correctamente")
        return redirect(to='Mantenedor')  # Redirigir a la página de lista de productos
    
    return render(request, 'administrador/EliminarProducto.html', {'producto': producto})

@staff_member_required  
def EditarProducto(request, id):
    
    producto = Producto.objects.get(id_prod=id)
    
    data = {
        'form': AddProductoForm(instance=producto),
        'prod':producto,
    }
    
    if request.method == 'POST':
        formulario = AddProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            return redirect(to="Mantenedor")
        data["form"] = formulario
        
    return render(request, 'administrador/EditarProducto.html', data)

#Creacion de usuarios


# def Registrarse(request):
#     context={}
#     formulario =
#     if formulario.is_valid:
#         formulario.save()
#         context={'mensaje': "Usuario registrado"}