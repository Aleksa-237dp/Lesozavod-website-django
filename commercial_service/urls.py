# Импортируем необходимые модули для маршрутизации
from django.urls import path
from . import views

# Указываем имя приложения для маршрутов
app_name = "commercial_service"

# Определяем маршруты для приложения
urlpatterns = [
    
    # Путь для главной страницы коммерческой службы
    path("", views.commercial, name="commercial"),

    # Путь для страницы клиентов
    path("clients/", views.clients, name="clients"),

    # Путь для создания нового клиента
    path("create-client/", views.create_client, name="create_client"),

]
