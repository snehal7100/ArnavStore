from django.shortcuts import render,redirect
from django.contrib import messages
from Login.models import LoginForm


def Login(request):
    return render(request,"Component/index.html")


def index(request):
    return render(request, 'index.html')
