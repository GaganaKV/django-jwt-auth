from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer


# ----------------- HTML TEMPLATE VIEWS -----------------
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'users/register.html', {'message': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'message': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'users/login.html', {'message': 'Invalid credentials'})

    return render(request, 'users/login.html')


@login_required(login_url='login')
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


# ----------------- API VIEWS (JWT) -----------------
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })
