from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('login',views.login, name='login'),
    path('registrar',views.registrar, name='registrar'),
    path('Producto/<int:id>',views.ProductoById, name='Producto'),
    path('Mantenedor',views.MantenedorProd, name='Mantenedor'),
    path('AgregarProducto', views.AgregarProducto, name='AgregarProducto'),
    path('EliminarProducto/<int:id>',views.EliminarProducto, name='EliminarProducto'),
    path('EditarProducto/<int:id>',views.EditarProducto, name='EditarProducto'),
    
]