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
        texts = Text.objects.all()
        if request.method == "POST" and request.POST.get("font-size") is not None:
            if request.POST.get("font-type", "reg") == "reg":
                a = "reg"
            elif request.POST.get("font-type", "reg") == "bold":
                a = "bold"
            elif request.POST.get("font-type", "reg") == "italic":
                a = "italic"
            else:
                a = "bold italic"
            form = TextForm(
                data={"name": request.POST.get("name"),
                      "text": request.POST.get("text"),
                      "font_size": request.POST.get("font-size"),
                      "font_family": request.POST.get("font-family"),
                      "font_type": a,
                      "theme_type": request.POST.get("theme")}
            )
            if form.is_valid():
                text = form.save(commit=False)
                text.user = request.user
                text.save()
                return render(request, 'Index.html',
                              {
                                  "username": request.user.username,
                                  "authenticated": request.user.is_authenticated
                              }
                              )
            else:
                return render(request, 'Notepad.html',
                              {'user': request.user, 'username': request.user.username, 'authenticated': True, "texts": texts})
        elif request.method == "POST":
            text = Text.objects.get(name=request.POST.get("txt"))
            if text.font_type == "bold":
                is_bold = True
                is_italic = False
            elif text.font_type == "italic":
                is_bold = False
                is_italic = True
            elif text.font_type == "bold italic":
                is_bold = True
                is_italic = True
            else:
                is_bold, is_italic = False, False
            print(text, is_bold, is_italic, str(text.font_size), text.text)
            return render(request, 'Note.html', {"font_size": str(text.font_size), "text_of": text.text, "is_bold": is_bold, "is_italic": is_italic, 'username': request.user.username, 'authenticated': True, "texts": texts})
        return render(request, 'Notepad.html',
                      {'user': request.user, 'username': request.user.username, 'authenticated': True, "texts": texts})


def note(request):
    return render(request, 'Note.html')
