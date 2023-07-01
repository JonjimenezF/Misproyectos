from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('Login',views.Login, name='Login'),
    path('Registrarse',views.Registrarse, name='Registrarse'),
    path('Producto/<int:id>',views.ProductoById, name='Producto'),
    path('Mantenedor',views.MantenedorProd, name='Mantenedor'),
    path('AgregarProducto', views.AgregarProducto, name='AgregarProducto'),
    path('EliminarProducto/<int:id>',views.EliminarProducto, name='EliminarProducto'),
    path('EditarProducto/<int:id>',views.EditarProducto, name='EditarProducto'),
    
]