# Импортируем необходимые модули и модели для работы с формами
from django import forms
from .models import CommercialServiceInfoClientsOfThePlant

# Определяем форму для создания/редактирования клиентов
class ClientForm(forms.ModelForm):
    class Meta:

        # Указываем, что форма будет связана с моделью CommercialServiceInfoClientsOfThePlant
        model = CommercialServiceInfoClientsOfThePlant

        # Определяем, какие поля модели будут включены в форму
        fields = [
            "name",
        ]

        # Задаем метку для поля 'name', которая будет отображаться в форме
        labels = {
            "name": "Клиент",
        }

        # Задаем виджет для поля 'name' с плейсхолдером
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
        }

