from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    data={'title':'Главная страница'}
    return render(request,'todoapp/index.html',context=data)


def page_not_found(request, exception):
    '''
    Функция обработчика исключения, когда страница не найдена
    '''
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
