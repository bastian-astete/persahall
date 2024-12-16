from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .models import Producto
from .forms import PedidoForm
from django.utils.timezone import now
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'accounts/login.html')

@login_required(login_url='/accounts/login/')
def home_view(request):
    productos_top_vistos = Producto.objects.all().order_by('-views')[:4]
    productos_recientes = Producto.objects.all().order_by('-fecha_creacion')[:10]
    
    context = {
        'productos_top_vistos': productos_top_vistos,
        'productos_recientes': productos_recientes,
    }
    return render(request, 'ecommerce/home.html', context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.views += 1
    producto.save()
    return render(request, 'ecommerce/detalle_producto.html', {'producto': producto})

@login_required
def realizar_pedido(request, producto_id=None):
    if producto_id:
        producto = Producto.objects.get(id=producto_id)
    else:
        producto = None

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = request.user
            pedido.save()
            return redirect('home')
    else:
        form = PedidoForm()

    return render(request, 'ecommerce/realizar_pedido.html', {'form': form, 'producto': producto})
