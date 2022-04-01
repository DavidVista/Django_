from django.shortcuts import render
from reapp.models import Text, Font


# Create your views here.

def main_page(request):
    texts = Text.objects.all()
    data = []
    tm = []
    for text in texts:
        bg_color = text.theme_type.split()[0]
        color = text.theme_type.split()[1]
        font_family = text.font.family
        size = text.font_size
        f = text.font.family.replace(" ", "+")
        t = text.font.type
        if t == "reg":
            t = ""
            w = str(text.font.weight)
        if t == "ital":
            t += ","
            w = "1," + str(text.font.weight)
        url = "@import url(https://fonts.googleapis.com/css2?family=" + f + ":" + t + "wght@" + w + "&display=swap);"
        data.append([url, font_family, text.name, text.text, bg_color, color, size])
    return render(request, "base_index.html", {"data": data})
