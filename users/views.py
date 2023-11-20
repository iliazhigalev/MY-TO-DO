from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth


def login(request):
    ''' Функция для авторизации и аунтефикации '''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:  # если пользователь у нас есть
                auth.login(request, user)  # мы его авторизуем
                return HttpResponseRedirect(reverse('todoapp:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout_user(request):
    return HttpResponse("logout")


def register(request):
    ''' Функция для регистрации пользователя '''
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:index'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
