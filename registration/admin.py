# Импортируем необходимые модули для админки
from django.contrib import admin
from .models import Profile

# Регистрация модели Profile в админке с настройками отображения
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    # Отображаем поле роли в списке профилей
    list_display = [
        "role",
    ]
    
    # Делаем поле роли кликабельным для перехода к редактированию
    list_display_links = [
        "role",
    ]


# Регистрация модели User в админке с настройками отображения для формы регистрации
class Register(admin.ModelAdmin):
    
    # Отображаем поля в списке регистрации
    list_display = [
        "username",
        "email",
        "password",
    ]

# Функция проверки, является ли пользователь сотрудником коммерческой службы
def is_commercial_staff(user):
    return user.groups.filter(name='Сотрудник коммерческой службы').exists()

# Функция проверки, является ли пользователь сотрудником службы производства
def is_production_staff(user):
    return user.groups.filter(name='Сотрудник службы производства').exists()

# Функция проверки, является ли пользователь сотрудником технологической службы
def is_tech_staff(user):
    return user.groups.filter(name='Сотрудник службы технологической').exists()

# Функция проверки, является ли пользователь клиентом
def is_client(user):
    return user.groups.filter(name='Клиент').exists()
