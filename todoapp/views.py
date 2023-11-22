from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
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
        # Устанавливаем пользователя перед сохранением формы
        form.instance.user = self.request.user
        form.instance.is_complete = False  # Инициализация значения is_complete
        return super(ToDoCreateView, self).form_valid(form)


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
