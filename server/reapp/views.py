import datetime

from django.shortcuts import render, redirect
from reapp.models import Text
from reapp.form import RegistrationUser, TextForm
import django.contrib.messages as messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
    if request.user.is_authenticated:
        form = TextForm()
        if request.method == "POST":
            print(request.POST)
            print(request.POST.get("font-type"))
            if request.POST.get("font-type", "reg") == "reg":
                a = "reg"
                is_bold = False
                is_italic = False
            elif request.POST.get("font-type", "reg") == "bold":
                a = "bold"
                is_bold = True
                is_italic = False
            elif request.POST.get("font-type", "reg") == "italic":
                a = "italic"
                is_bold = False
                is_italic = True
            else:
                a = "bold italic"
                is_bold = True
                is_italic = True
            if request.POST.get("theme") == "Light":
                b = "white black"
            elif request.POST.get("theme") == "Dark":
                b = "black white"
            elif request.POST.get("theme") == "Monokai":
                b = "black red"
            else:
                b = "brown yellow"
            form = TextForm(
                data={"name": request.POST.get("name"),
                      "text": request.POST.get("text"),
                      "font_size": request.POST.get("font-size"),
                      "font_family": request.POST.get("font-family"),
                      "font_type": a,
                      "theme_type": b}
            )
            if form.is_valid():
                text = form.save(commit=False)
                text.user = request.user
                text.save()
                print("I'm here!")
                return render(request, 'Note.html',
                              {
                                  'font_size': request.POST.get("font-size"),
                                  'is_bold': is_bold, 'is_italic': is_italic,
                                  'font-family': request.POST.get("font-family")[0],
                                  'theme': request.POST.get("theme"),
                                  'header': request.POST.get("header"),
                                  'text': request.POST.get("text"),
                                  # 'texts': texts,
                                  'user': request.user,
                                  'username': request.user.username,
                                  'authenticated': True
                              }
                              )
            else:
                print(form.errors.as_data())
        return render(request, 'Notepad.html',
                      {'user': request.user, 'username': request.user.username, 'authenticated': True})


def note(request):
    return render(request, 'Note.html')
