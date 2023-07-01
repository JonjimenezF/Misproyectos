from django.forms import ModelForm
from .models import Producto
class AddProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id_prod', 'nombre_prod', 'precio_prod', 'img_prod']