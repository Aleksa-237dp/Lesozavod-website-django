"""
URL configuration for lesozavod project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Импорт необходимых модулей из Django
from django.contrib import admin
from django.urls import path, include


# Определение маршрутов URL для проекта
urlpatterns = [
    
    # Путь для административной панели Django
    path("admin/", admin.site.urls),

    # Включение маршрутов из приложения "services"
    path("", include("services.urls")),

    # Включение маршрутов из приложения "registration"
    path("registration/", include("registration.urls")),

    # Включение маршрутов из приложения "commercial_service"
    path('commercial_service/', include('commercial_service.urls')),
    
    # Включение маршрутов из приложения "production_service"
    path('production_service/', include('production_service.urls')),
    
    # Включение маршрутов из приложения "technologist_service"
    path('technologist_service/', include('technologist_service.urls')),

]
