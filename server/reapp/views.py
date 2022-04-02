from django.shortcuts import render, redirect
from reapp.models import Text, Font
from reapp.form import RegistrationUser
import django.contrib.messages as messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def main_page(request):
    authenticated = request.user.is_authenticated
    if authenticated:
        username = request.user.username
        return render(request, "Index.html", {'authenticated': authenticated, 'username': username})
    return render(request, "Index.html", {'authenticated': authenticated})


def faq_page(request):
    authenticated = request.user.is_authenticated
    if authenticated:
        username = request.user.username
        return render(request, "FAQ.html", {'authenticated': authenticated, 'username': username})
    return render(request, "FAQ.html")


def info_page(request):
    authenticated = request.user.is_authenticated
    if authenticated:
        username = request.user.username
        return render(request, "Info.html", {'authenticated': authenticated, 'username': username})
    return render(request, "Info.html")


def registration_page(request):
    if request.user.is_authenticated:
        return render(request, 'Index.html', {'authenticated': True, 'username': request.user.username})
    form = RegistrationUser()
    if request.method == "POST":
        form = RegistrationUser(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Index.html', {'authenticated': True, 'username': request.POST.get("username")})
        else:
            messages.error(request, "Форма регистрации заполнена неверно!")
            return render(request, "Registration.html")

    return render(request, "Registration.html", {"form": form})


def login_page(request):
    if request.user.is_authenticated:
        return render(request, 'Index.html', {'authenticated': True, 'username': request.user.username})
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'Index.html', {'authenticated': True, 'username': request.user.username})
        else:
            messages.error(request, 'Неверный логин или пароль!')

    return render(request, "Login.html")


def logout_page(request):
    logout(request)
    return render(request, 'Index.html', {'authenticated': False, 'username': None})


def notepad(request):
    return render(request, 'Notepad.html', {'user': request.user, 'username': request.user.username, 'authenticated': True})