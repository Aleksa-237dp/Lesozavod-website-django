# Импортируем необходимые модули для маршрутизации
from django.urls import path
from . import views

# Устанавливаем пространство имен для URL-ов приложения
app_name = "services"

# Определяем маршруты URL для приложения "services"
urlpatterns = [

    # Маршрут для главной страницы сервиса
    path("", views.index_service, name="index"),

]
