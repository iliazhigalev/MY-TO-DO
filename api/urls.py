from django.urls import path
from api.views import ToDoListAPIView, ToDoDetailAPIView

app_name = 'api'

urlpatterns = [
    path('api/todo/', ToDoListAPIView.as_view(), name='todo-list'),
    path('api/todo/<int:pk>/', ToDoDetailAPIView.as_view(), name='todo-detail'),
]
