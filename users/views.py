from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
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


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:index'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/profile.html', context)


def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('todoapp:index'))
