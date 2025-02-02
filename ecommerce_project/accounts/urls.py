from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)