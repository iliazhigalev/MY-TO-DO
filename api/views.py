from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todoapp.models import ToDo
from todoapp.serializers import ToDoSerializer

class ToDoListAPIView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

