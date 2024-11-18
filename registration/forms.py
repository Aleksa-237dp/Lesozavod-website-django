# Импортируем необходимые модули и модели для работы с формами
from django import forms
from .models import Profile
from django.contrib.auth.models import User

# Форма для регистрации нового пользователя
class RegisterForm(forms.ModelForm):
    
    class Meta:

        # Указываем модель, с которой будет связана форма
        model = User
        
        # Поля формы
        fields = ['username', 'email', 'password']

        widgets = {

            # Плейсхолдер для имени
            'username': forms.TextInput(attrs={'placeholder': 'Имя Фамилия'}),
            
            # Плейсхолдер для пароля
            'password': forms.PasswordInput(attrs={'placeholder': '••••••••'}),
            
            # Плейсхолдер для email
            'email': forms.TextInput(attrs={'placeholder': 'name@example.com'}),
        }

        # Убираем текст помощи для имени пользователя
        help_texts = {
            'username': '',
        }

# Форма для редактирования профиля пользователя
class ProfileForm(forms.ModelForm):

    class Meta:

        # Указываем модель, с которой будет связана форма
        model = Profile

        # Поля формы
        fields = ['role', 'avatar', 'phone', 'extra_info',]

        widgets = {
            # Плейсхолдер для телефона
            'phone': forms.TextInput(attrs={'placeholder': '+7 *** *** ** **'}),
            
            # Поля для дополнительной информации (многострочное)
            'extra_info': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
        
    