# Импортируем необходимые модули и модели для работы с формами
from django import forms
from .models import TechnologistServiceInfoTypesOfForestProducts

# Определяем форму для работы с моделью 
class ProductForm(forms.ModelForm):
    class Meta:

        # Указываем, что форма связана с моделью TechnologistServiceInfoTypesOfForestProducts
        model = TechnologistServiceInfoTypesOfForestProducts

        # Указываем поля, которые будут включены в форму
        fields = [
            "name",
            "description",
            "price_per_piece",
        ]

        # Задаем метки для полей формы
        labels = {
            "name": "Название лесопродукции",
            "description": "Описание лесопродукции",
            "price_per_piece": "Цена за штуку",
        }

        # Настройка виджетов для полей формы
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Вид'}),
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40,'placeholder': 'Обязательное поле'}),
            'price_per_piece': forms.NumberInput(attrs={'placeholder': 'число'}),
        }