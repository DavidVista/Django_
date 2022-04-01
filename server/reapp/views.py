from django.shortcuts import render
from reapp.models import Text, Font


# Create your views here.

def main_page(request):
    return render(request, "Index.html")


def faq_page(request):
    return render(request, "FAQ.html")


def info_page(request):
    return render(request, "Info.html")
