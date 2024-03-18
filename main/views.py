from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from goods.models import Categories

def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели НаДиване',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'текст о том, почему этот магазин такой классный, и почему тут лучший товар'
    }
    return render(request, 'main/about.html', context)
