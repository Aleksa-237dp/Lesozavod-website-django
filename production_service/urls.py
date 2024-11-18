# Импортируем необходимые модули для маршрутизации
from django.urls import path
from . import views

# Указываем имя приложения для маршрутов
app_name = "production_service"

# Определяем маршруты для приложения
urlpatterns = [

    # Главная страница приложения
    path("", views.production, name="production"),

    # Страница для регистрации нового заказа
    path("register-order/", views.register_order, name="register_order"),
    
    # Страница со списком всех заказов
    path('orders/', views.orders, name='orders'),
    
]
