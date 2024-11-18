# Импортируем класс AppConfig для настройки приложения
from django.apps import AppConfig


# Определяем конфигурацию приложения
class ServiceConfig(AppConfig):

    # Указываем тип поля по умолчанию
    default_auto_field = "django.db.models.BigAutoField"

    # Имя приложения
    name = "services"
