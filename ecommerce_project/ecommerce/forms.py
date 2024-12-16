from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cantidad', 'direccion_envio', 'telefono_contacto']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'direccion_envio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control'}),
        }