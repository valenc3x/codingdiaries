from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def landing(request):
    template_vars = {}
    return render(
        request,
        'landing.html',
        context=template_vars
    )

@login_required
def home(request):
    template_vars = {}
    return render(
        request,
        'home.html',
        context=template_vars
    )

def login_user(request):
    template_vars = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home')
            else:
                template_vars['error'] = 'Disabled Account'
        else:
            template_vars['error'] = 'Login error'
    return render(
        request,
        'login.html',
        context=template_vars
    )

def logout_user(request):
    logout(request)
    return redirect('/login')
