from django.shortcuts import render, redirect
from reapp.models import Text, Font
from reapp.form import RegistrationUser
import django.contrib.messages as messages
from django.contrib.auth import authenticate, login


# Create your views here.

def main_page(request):
    return render(request, "Index.html")


def faq_page(request):
    return render(request, "FAQ.html")


def info_page(request):
    return render(request, "Info.html")


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('')
    form = RegistrationUser()
    if request.method == "POST":
        form = RegistrationUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            messages.error(request, "Форма регистрации заполнена неверно!")
            return render(request, "Registration.html")

    return render(request, "Registration.html", {"form": form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('')
        else:
            messages.error(request, 'Неверный логин или пароль!')
            return()

    return render(request, "Login.html")