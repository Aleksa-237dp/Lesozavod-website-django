# Импортируем необходимые модули и классы из Django
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest
from .models import TechnologistServiceInfoTypesOfForestProducts
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


# Функция для обработки запроса на страницу технолога
def technologist(
        request: HttpRequest # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответа
    
    # Отображаем шаблон "technologist.html" для страницы технолога
    return render(request, "technologist_service/technologist.html")


# Декоратор @login_required ограничивает доступ к функции только авторизованным пользователям.
# Если пользователь не авторизован, он будет перенаправлен на страницу входа.
@login_required

# Функция для обработки запроса на страницу лесопродукции
def products(
        request: HttpRequest # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответа
    
    # Получаем все объекты лесопродукции из базы данных
    products = TechnologistServiceInfoTypesOfForestProducts.objects.all()

    # Передаем форму в контекст для шаблона
    context = {
        "products": products,
        }

    # Отображаем шаблон "products.html" и передаем список продуктов в контексте
    return render(request, "technologist_service/products.html", context = context)



# Функция для обработки создания нового вида лесопродукции
def create_products(
        request: HttpRequest, # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответа
    
    # Проверяем, был ли отправлен POST-запрос
    if request.method == "POST":

        # Создаем форму с данными из запроса
        form = ProductForm(request.POST)

        # Проверяем, валидна ли форма
        if form.is_valid():
            
            # Сохраняем данные в базе данных
            form.save()
            
            # Получаем URL для редиректа
            url = reverse("technologist_service:products")

            # Перенаправляем на страницу со списком лесопродукции
            return redirect(url)
        else:
            
            # Выводим сообщение об ошибке
            print("Данные не валидны")

            # Выводим данные формы для отладки
            print(form.data)
    else:
        # Если не POST-запрос, создаем пустую форму
        form = ProductForm

    # Передаем форму в контекст для шаблона
    context = {
        "form": form,
        }
    
    # Отображаем шаблон с формой
    return render(request, "technologist_service/create-products.html", context = context)


