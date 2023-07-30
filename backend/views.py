from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class login_view(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print("\nUsername = ",username,"\nPassword = ",password,"\n")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            user_details = {
                'username': user.username
            }
            return JsonResponse({'message': 'Login successful !', 'user': user_details}, status=200)
        else:
            return JsonResponse({'message': 'Login unsuccessful !'}, status=401)
    

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def staff(request):
    return render(request, 'index.html')

def report(request):
    return render(request, 'index.html')

def signup(request):
    return redirect('/')
