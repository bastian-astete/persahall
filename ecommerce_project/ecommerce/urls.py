from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import realizar_pedido

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('comprar/<int:producto_id>/', realizar_pedido, name='realizar_pedido'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)