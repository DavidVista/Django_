from django.shortcuts import render
from reapp.models import Text
from reapp.form import RegistrationUser, TextForm
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


def note(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.POST.get("font_size") is not None and request.POST.get("new_sheet") is None:
            req_text = False
            status = request.POST.get("status")
            if status == "Saved":
                is_required = True
            else:
                is_required = False
            if request.POST.getlist("font_type") == ["reg"]:
                a = "reg"
            elif request.POST.getlist("font_type") == ["reg", "bold"]:
                a = "bold"
            elif request.POST.getlist("font_type") == ["reg", "italic"]:
                a = "italic"
            else:
                a = "bold italic"
            if Text.objects.filter(name=request.POST.get("name")).exists() and not is_required:
                texts = Text.objects.all()
                messages.error(request, "Такая запись уже существует!")
                return render(request, "Note.html",
                              {'user': request.user, 'username': request.user.username, 'authenticated': True,
                               "texts": texts, "req_text": req_text})
            elif is_required:
                obj = Text.objects.get(name=request.POST.get("old_name"))
                obj.delete()
                form = TextForm(data={
                    "name": request.POST.get("name"),
                    "text": request.POST.get("text"),
                    "font_size": request.POST.get("font_size"),
                    "font_family": request.POST.get("font_family"),
                    "font_type": a,
                    "theme_type": request.POST.get("theme")
                }
                )
            else:
                form = TextForm(
                    data={"name": request.POST.get("name"),
                          "text": request.POST.get("text"),
                          "font_size": request.POST.get("font_size"),
                          "font_family": request.POST.get("font_family"),
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
                texts = Text.objects.all()
                messages.error(request, "Что-то пошло не так, просим извинений!")
                return render(request, 'Note.html',
                              {'user': request.user, 'username': request.user.username, 'authenticated': True,
                               "texts": texts, "req_text": req_text})
        elif request.method == "POST" and request.POST.get("txt") is not None:
            req_text = True
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
            texts = Text.objects.all()
            return render(request, 'Note.html',
                          {"text": text, "font_size": text.font_size, "text_of": text.text, "is_bold": is_bold,
                           "is_italic": is_italic, 'username': request.user.username, 'authenticated': True,
                           "texts": texts, "req_text": req_text})
        elif request.method == "POST" and request.POST.get("is_deleted") is not None:
            req_text = False
            text = Text.objects.get(name=request.POST.get("is_deleted"))
            text.delete()
            texts = Text.objects.all()
            messages.success(request, "Записка успешно удалена!")
            return render(request, 'Note.html',
                          {'user': request.user, 'username': request.user.username, 'authenticated': True,
                           "texts": texts, "req_text": req_text})
        req_text = False
        texts = Text.objects.all()
        print("I'm here!")
        return render(request, 'Note.html',
                      {'user': request.user, 'username': request.user.username, 'authenticated': True, "texts": texts,
                       "req_text": req_text})
