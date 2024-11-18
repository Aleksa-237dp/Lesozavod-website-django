# Импортируем необходимые модули для админки
from django.contrib import admin
from .models import CommercialServiceInfoClientsOfThePlant

# Регистрация модели CommercialServiceInfoClientsOfThePlant в админке
@admin.register(CommercialServiceInfoClientsOfThePlant)
class CommercialServiceInfoClientsOfThePlantAdmin(admin.ModelAdmin):

    # Определяем, какие поля будут отображаться в списке объектов модели в админке
    list_display = [
        "name",
    ]
    
    # Указываем, что поле 'name' будет являться ссылкой на страницу редактирования объекта
    list_display_links = [
        "name",
    ]

