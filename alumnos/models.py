from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name="Id Usuario")
    nombre_usuario = models.CharField(max_length=50, verbose_name="Nombre de Usuario")
    email_usuario = models.CharField(max_length=50, verbose_name="Email")
    contraseña_usuario = models.CharField(max_length=50, verbose_name="Contraseña")
    
    def __str__(self):
        return self.nombre_usuario

class Producto(models.Model):
    id_prod = models.IntegerField(primary_key=True, verbose_name="Id Producto") 
    nombre_prod = models.CharField(max_length=100, verbose_name="Nombre Producto")
    precio_prod = models.IntegerField(verbose_name="Precio Producto")
    img_prod = models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen")

    
    def __str__(self):
        return self.nombre_prod

class Compra(models.Model):
    id_compra = models.IntegerField(primary_key=True, verbose_name="Id Compra")
    fecha_compra = models.DateField(verbose_name="Fecha Compra")
    desc_compra = models.CharField(max_length=1000, verbose_name="Descripción compra", default="")
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Id Producto", default="0")
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Id Usuario", default="0")

    def __str__(self):
        return self.desc_compra