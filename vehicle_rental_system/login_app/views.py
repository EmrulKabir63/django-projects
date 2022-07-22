from django.shortcuts import render

# Create your views here.

def admin_login(request):
    dict = {}
    return render(request, 'login_app/admin_login.html', context=dict)

def contact(request):
    dict = {}
    return render(request, 'login_app/contact.html', context=dict)

def home(request):
    dict = {}
    return render(request, 'login_app/home.html', context=dict)

def register(request):
    dict = {}
    return render(request, 'login_app/register.html', context=dict)

def user_login(request):
    dict = {}
    return render(request, 'login_app/user_login.html', context=dict)