from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    ''' Форма для входа пользователей'''

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    ''' Форма для регистрации пользователей'''

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    '''Форма для обновления профиля '''

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email',)
