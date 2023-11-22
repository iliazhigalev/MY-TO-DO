from django.db import models
from users.models import User

class ToDo(models.Model):
    ''' Класс, описывающий модель приложения в бд '''

    title = models.CharField(max_length=150, verbose_name='Название задания')
    is_complete = models.BooleanField('Завершено', default=False)
    time = models.DateTimeField(auto_now_add=True,verbose_name='дата создания')  # дата, создания задания
    user=models.ForeignKey(to=User,on_delete=models.CASCADE,null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
