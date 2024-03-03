from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели НаДиване',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'текст о том, почему этот магазин такой классный, и почему тут лучший товар'
    }
    return render(request, 'main/about.html', context)
