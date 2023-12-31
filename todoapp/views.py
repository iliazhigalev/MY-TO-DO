from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from rest_framework import generics

from users.models import User
from .forms import ToDoForm
from .models import ToDo
from django.views.generic.edit import CreateView, DeleteView

class IndexView(ListView):
    model = ToDo
    template_name = 'todoapp/index.html'
    title = "Главная страница"
    ordering = ['-id']  # Указывает порядок сортировки


class ToDoCreateView(CreateView):
    model = ToDo
    template_name = 'todoapp/index.html'
    form_class = ToDoForm
    success_url = reverse_lazy('todoapp:index')

    def form_valid(self, form):
        # Получаем пользователя из запроса
        user = self.request.user
        User = get_user_model()
        title = form.cleaned_data.get('title', False)

        if user.is_authenticated and isinstance(user, User) and title:
            form.instance.user = user
            form.instance.is_complete = False
            return super().form_valid(form)
        else:
            return HttpResponse("<h1>Статьи по категориям</h1>")


def update(request, pk):
    '''Класс обновления задания'''
    todo = ToDo.objects.get(id=pk)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('todoapp:index')


class ToDoDeleteView(DeleteView):
    '''Класс удаления задания задания'''
    model = ToDo
    template_name = 'todoapp/index.html'
    success_url = reverse_lazy('todoapp:index')


def page_not_found(request, exception):
    '''
    Функция обработчика исключения, когда страница не найдена
    '''
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
