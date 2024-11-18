# Импортируем необходимые модули для админки
from django.contrib import admin
from .models import ProductionServiceOrder

# Регистрируем модель ProductionServiceOrder в админке
@admin.register(ProductionServiceOrder)
class ProductionServiceOrderAdmin(admin.ModelAdmin):

    # Поля, отображаемые в списке заказов
    list_display = [
        "registration_date",
        "deadline_date",
        "info_client",
        "product",
        "product_quantity",
        "extra_info",
    ]

    # Поля, по которым можно фильтровать заказы
    list_filter = [
        "info_client",
        "product",
    ]
    
    # Метод, который позволяет изменить запрос к базе данных (например, для добавления сортировки, фильтрации)
    # В данном случае он возвращает стандартный запрос, ничего не меняя
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
    