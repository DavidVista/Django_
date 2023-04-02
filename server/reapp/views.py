from django.shortcuts import render
from reapp.models import Text, Font
from reapp.form import RegistrationUser, TextForm, FontForm
import django.contrib.messages as messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def main_page(request):
    authenticated = request.user.is_authenticated
    if authenticated:
        f = Font.objects.all()
        if not bool(f):
            stand_font1 = FontForm(
                data={"family": "Vollkorn", "url": "https://fonts.googleapis.com/css2?family=Vollkorn&display=swap"})
            if stand_font1.is_valid():
                stand_font1.save()

            stand_font2 = FontForm(
                data={"family": "Red Hat Mono",
                      "url": "https://fonts.googleapis.com/css2?family=Red+Hat+Mono:wght@300&display=swap"})
            if stand_font2.is_valid():
                stand_font2.save()

            stand_font3 = FontForm(
                data={"family": "Roboto Slab",
                      "url": "https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100&display=swap"})
            if stand_font3.is_valid():
                stand_font3.save()

            stand_font4 = FontForm(
                data={"family": "Open Sans",
                      "url": "https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap"})
            if stand_font4.is_valid():
                stand_font4.save()

        username = request.user.username
        fonts = Font.objects.all()
        return render(request, "Index.html", {'authenticated': authenticated, 'username': username, "fonts": fonts})
    fonts = Font.objects.all()
    return render(request, "Index.html", {'authenticated': authenticated, "fonts": fonts})


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
        fonts = Font.objects.all()
        return render(request, 'Index.html', {'authenticated': True, 'username': request.user.username, "fonts": fonts})
    form = RegistrationUser()
    if request.method == "POST":
        form = RegistrationUser(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(request, username=request.POST.get("username"),
                                    password=request.POST.get("password1"))
            login(request, new_user)
            fonts = Font.objects.all()
            return render(request, 'Index.html',
                          {'authenticated': True, 'username': request.POST.get("username"), "fonts": fonts})
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
            fonts = Font.objects.all()
            return render(request, 'Index.html',
                          {'authenticated': True, 'username': request.user.username, "fonts": fonts})
        else:
            messages.error(request, 'Неверный логин или пароль!')

    return render(request, "Login.html")


def logout_page(request):
    logout(request)
    fonts = Font.objects.all()
    return render(request, 'Index.html', {'authenticated': False, 'username': None, "fonts": fonts})


def note(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.POST.get("font_size") is not None and request.POST.get(
                "new_sheet") is None and request.POST.get("link") is '':
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
                fonts_ = Font.objects.all()
                fonts = []
                for f in fonts_:
                    family = "".join(f.family.split())
                    fonts.append([f, family])
                messages.error(request, "Такая запись уже существует!")
                return render(request, "Note.html",
                              {'user': request.user, 'username': request.user.username, 'authenticated': True,
                               "texts": texts, "req_text": req_text, "fonts": fonts})
            elif is_required:
                obj = Text.objects.get(name=request.POST.get("old_name"))
                obj.delete()
                form = TextForm(data={
                    "name": request.POST.get("name"),
                    "text": request.POST.get("text"),
                    "font_size": request.POST.get("font_size"),
                    "font_type": a,
                    "theme_type": request.POST.get("theme")
                }
                )
                if form.is_valid():
                    text = form.save(commit=False)
                    text.user = request.user
                    text.font_family = Font.objects.get(family=request.POST.get("font_family"))
                    text.save()
                    fonts = Font.objects.all()
                    return render(request, 'Index.html',
                                  {
                                      "username": request.user.username,
                                      "authenticated": request.user.is_authenticated,
                                      "fonts": fonts
                                  }
                                  )
            else:
                form = TextForm(
                    data={"name": request.POST.get("name"),
                          "text": request.POST.get("text"),
                          "font_size": request.POST.get("font_size"),
                          "font_type": a,
                          "theme_type": request.POST.get("theme")}
                )
                if form.is_valid():
                    text = form.save(commit=False)
                    text.user = request.user
                    text.font_family = Font.objects.get(family=request.POST.get("font_family"))
                    text.save()
                    fonts = Font.objects.all()
                    return render(request, 'Index.html',
                                  {
                                      "username": request.user.username,
                                      "authenticated": request.user.is_authenticated,
                                      "fonts": fonts
                                  }
                                  )
                else:
                    texts = Text.objects.all()
                    fonts_ = Font.objects.all()
                    fonts = []
                    for f in fonts_:
                        family = "".join(f.family.split())
                        fonts.append([f, family])
                    messages.error(request, "Что-то пошло не так, просим извинений!")
                    return render(request, 'Note.html',
                                  {'user': request.user, 'username': request.user.username, 'authenticated': True,
                                   "texts": texts, "req_text": req_text, "fonts": fonts})
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
            fonts_ = Font.objects.all()
            fonts = []
            for f in fonts_:
                family = "".join(f.family.split())
                fonts.append([f, family])
            return render(request, 'Note.html',
                          {"text": text, "font_size": text.font_size, "text_of": text.text, "is_bold": is_bold,
                           "is_italic": is_italic, 'username': request.user.username, 'authenticated': True,
                           "texts": texts, "req_text": req_text, "fonts": fonts})
        elif request.method == "POST" and request.POST.get("is_deleted") is not None:
            req_text = False
            text = Text.objects.get(name=request.POST.get("is_deleted"))
            text.delete()
            texts = Text.objects.all()
            fonts_ = Font.objects.all()
            fonts = []
            for f in fonts_:
                family = "".join(f.family.split())
                fonts.append([f, family])
            messages.success(request, "Записка успешно удалена!")
            return render(request, 'Note.html',
                          {'user': request.user, 'username': request.user.username, 'authenticated': True,
                           "texts": texts, "req_text": req_text, "fonts": fonts})
        elif request.method == "POST" and request.POST.get("link") is not '':
            req_text = False
            texts = Text.objects.all()
            url = request.POST.get("link")
            u = url[41:][:-13].split(":")[0]
            u = " ".join(u.split("+"))
            form = FontForm(data={
                "url": url,
                "family": u
            })
            if form.is_valid():
                form.save()
                fonts = Font.objects.all()
                return render(request, 'Index.html',
                              {'username': request.user.username, 'authenticated': True,
                               "fonts": fonts})
            else:
                messages.error(request,
                               "Указана некорректная ссылка на Google Fonts. Вставляйте, пожалуйста, только url (например: https://fonts.googleapis.com/...)")
                fonts_ = Font.objects.all()
                fonts = []
                for f in fonts_:
                    family = "".join(f.family.split())
                    fonts.append([f, family])
                return render(request, 'Note.html',
                              {'user': request.user, 'username': request.user.username, 'authenticated': True,
                               "texts": texts, "req_text": req_text, "fonts": fonts})
        req_text = False
        texts = Text.objects.all()
        fonts_ = Font.objects.all()
        fonts = []
        for f in fonts_:
            family = "".join(f.family.split())
            fonts.append([f, family])
        return render(request, 'Note.html',
                  {'user': request.user, 'username': request.user.username, 'authenticated': True, "texts": texts,
                   "req_text": req_text, "fonts": fonts})
