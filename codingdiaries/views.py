from django.contrib.auth import authenticate, login
from django.shortcuts import render

def landing(request):
    template_vars = {}
    return render(
        request,
        'landing.html',
        context=template_vars
    )

def home(request):
    template_vars = {}
    return render(
        request,
        'home.html',
        context=template_vars
    )

def login(request):
    template_vars = {}
    return render(
        request,
        'login.html',
        context=template_vars
    )
