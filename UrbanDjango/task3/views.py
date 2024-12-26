from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index1(request):
    title = 'Мой сайт'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/main_page.html', context)

def index2(request):
    title = 'Магазин'
    text = 'Игры'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/games.html', context)

def index3(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/basket.html', context)