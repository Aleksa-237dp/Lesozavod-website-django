# Импортируем необходимые модули для админки
from django.contrib import admin
from .models import TechnologistServiceInfoTypesOfForestProducts

# Регистрируем модель в админке
@admin.register(TechnologistServiceInfoTypesOfForestProducts)
class TechnologistServiceInfoTypesOfForestProductsAdmin(admin.ModelAdmin):

    # Указываем, какие поля отображать в списке в административной панели
    list_display = [

        "name",
        "description",
        "price_per_piece",
    ]
    
    # Указываем, какие поля будут ссылками в списке
    list_display_links = [
        "name",
    ]