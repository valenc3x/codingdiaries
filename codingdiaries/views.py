from django.shortcuts import render

def home(request):
    template_vars = {}
    return render(
        request,
        'home.html',
        context=template_vars
    )
