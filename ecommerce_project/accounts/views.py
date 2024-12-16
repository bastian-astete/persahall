from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    """
    Vista para manejar solicitudes de inicio de sesión.
    """
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        try:
            body = json.loads(request.body)
            username = body.get('username')
            password = body.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato de datos inválido'}, status=400)

        if not username or not password:
            return JsonResponse({'error': 'Por favor, completa todos los campos'}, status=400)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return JsonResponse({'redirect_url': '/ecommerce/home'}, status=200)
            else:
                return JsonResponse({'error': 'Cuenta desactivada. Contacta al administrador.'}, status=403)
        else:
            return JsonResponse({'error': 'Credenciales inválidas'}, status=401)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        full_name = request.POST.get('full_name')
        nickname = request.POST.get('nickname')
        birth_date = request.POST.get('birth_date')
        profile_picture = request.FILES.get('profile_picture')

        if password != password2:
            return JsonResponse({'error': 'Las contraseñas no coinciden'}, status=400)

        try:
            user = get_user_model().objects.create_user(
                username=username,
                email=email,
                password=password,
                full_name=full_name,
                nickname=nickname,
                birth_date=birth_date,
                profile_picture=profile_picture
            )
            return JsonResponse({'message': 'Usuario registrado exitosamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class LogoutView(APIView):
    def get(self, request):
        request.session.flush()
        logout(request)
        return redirect('login')

@login_required
def ecommerce_home(request):
    return render(request, 'ecommerce/home.html')