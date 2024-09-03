from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
# def login(request):
#     if request.method == "GET":
#         return render(request, 'login.html')
#     # elif request.method == "POST":
#     #     username = request.POST.get('username')
#     #     password = request.POST.get('password')
    
# def logout(request):
#     auth.logout(request)
#     return redirect(request, '/usuarios/login/')