from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'image', 'username', 'email',)
    list_display = ('username','last_name','image_admin','email',)

    @admin.display(description='Фото')
    def image_admin(self,user: User):
        if user.image:
            return mark_safe(f"<img src='{user.image.url}' width=50>")
        return 'Без фото'