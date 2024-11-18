# Импортируем необходимые модули для маршрутизации
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Указываем имя приложения для маршрутов
app_name = "registration"

# Определяем маршруты для приложения
urlpatterns = [
    
    path("login/", 
         # Используем готовое представление LoginView
         LoginView.as_view(
             
             # Указываем шаблон для входа
             template_name = "registration/login.html",

             # Перенаправляем авторизованных пользователей
             redirect_authenticated_user = True,
        ),
        name = "login", # Имя URL для ссылки
    ),

    # Используем готовое представление LogoutView
    path("logout/", LogoutView.as_view(), name="logout"),

    # Маршрут для регистрации
    path("register/", views.register, name="register"),

    # Маршрут для профиля
    path("profile/", views.profile, name="profile"),
]
