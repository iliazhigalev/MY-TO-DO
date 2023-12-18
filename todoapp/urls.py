from django.urls import path

from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.ToDoCreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.ToDoDeleteView.as_view(), name='delete')

]
