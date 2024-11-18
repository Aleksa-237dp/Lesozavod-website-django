# Импортируем необходимые модули для маршрутизации
from django.urls import path
from . import views

# Указываем имя приложения для маршрутов
app_name = "technologist_service"

# Определяем маршруты для приложения
urlpatterns = [

    # URL-адрес главной страницы о сотрудниках службы технолога
    path("", views.technologist, name="technologist"), 
    
    # URL-адрес страницы, на которой отображаются все виды лесопродукции
    path("products/", views.products, name="products"),

    # URL-адрес для страницы создания нового вида лесопродукции
    path("create-products/", views.create_products, name="create_products"),

]
