from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'spa_app/index.html')


def rooms(request):
    return render(request, 'spa_app/rooms.html')


def new2024(request):
    return render(request, 'spa_app/new2024.html')
