# Импортируем необходимые модули и модели для работы с формами
from django import forms
from .models import ProductionServiceOrder

# Определяем форму для создания и редактирования заказов
class OrderForm(forms.ModelForm):
    class Meta:

        # Указываем, что форма связана с моделью ProductionServiceOrder
        model = ProductionServiceOrder

        # Поля, которые будут отображаться в форме
        fields = [
            "registration_date",
            "deadline_date",
            "info_client",
            "product",
            "product_quantity",
            "extra_info",
            "status",
        ]

        # Подписи для полей формы
        labels = {
            "registration_date": "Дата регистрации заказа",
            "deadline_date": "Дата окончания",
            "info_client": "Информация о клиенте-заказчике",
            "product": "Вид лесопродукции",
            "product_quantity": "Количество лесопродукции",
            "extra_info": "Дополнительная информация о заказе",
            "status": "Статус заказа",
        }
        
        # Виджеты для полей формы (для изменения отображения в интерфейсе)
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'deadline_date': forms.DateInput(attrs={'type': 'date'}),
            'extra_info': forms.Textarea(attrs={'rows': 5, 'cols': 40,'placeholder': 'Обязательное поле'}),
            'info_client': forms.TextInput(attrs={'placeholder': 'Имя Фамилия'}),
            'product_quantity': forms.NumberInput(attrs={'placeholder': '(в штуках)'}),
        }

    # Метод для валидации формы
    def clean(self):

        # Вызываем метод валидации родительского класса
        cleaned_data = super().clean()

        # Получаем значения из очищенных данных
        deadline_date = cleaned_data.get("deadline_date")
        registration_date = cleaned_data.get("registration_date")
        quantity = cleaned_data.get("product_quantity")

        # Проверка, что дата окончания позже даты регистрации
        if deadline_date and registration_date and deadline_date <= registration_date:
            raise forms.ValidationError("Дата окончания должна быть позже даты регистрации.")

        if quantity and quantity <= 0:
            raise forms.ValidationError("Количество должно быть больше нуля.")

        return cleaned_data