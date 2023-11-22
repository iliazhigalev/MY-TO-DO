from django.contrib import admin
from .models import ToDo

@admin.register(ToDo)
class ToDoModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_complete','time','user')
    list_display_links = ('title',)# указываются поля, через которые могу открывать задания в админке
    list_editable = ('is_complete',)  # указываю поля, которые в админке можно редактировать, не переходя конкретно в задание
    list_per_page = 6 # настроил пагинацию в админке
