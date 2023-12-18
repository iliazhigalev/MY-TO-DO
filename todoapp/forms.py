from django import forms
from .models import ToDo

# class ToDoForm(forms.ModelForm):
#
#     class Meta:
#         model=ToDo
#         fields=['title',]
#         widgets={
#             'title':forms.TextInput()
#         }

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title']
        widgets = {'title': forms.TextInput()}

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title.strip():
            raise forms.ValidationError("Название задачи не может быть пустым.")
        return title