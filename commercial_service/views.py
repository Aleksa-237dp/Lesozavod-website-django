# Импорт необходимых модулей для представлений
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from .models import CommercialServiceInfoClientsOfThePlant
from .forms import ClientForm


# Функция для обработки запроса на страницу коммерческой службы
def commercial(
        request: HttpRequest # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответа
    
    # Отображаем шаблон "commercial.html" для страницы коммерческой службы
    return render(request, "commercial_service/commercial.html")


# Декоратор @login_required ограничивает доступ к функции только авторизованным пользователям.
# Если пользователь не авторизован, он будет перенаправлен на страницу входа.
@login_required
def clients(
        request: HttpRequest # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответа
    
    # Получение всех клиентов из модели CommercialServiceInfoClientsOfThePlant
    client = CommercialServiceInfoClientsOfThePlant.objects.all()
    
    # Отображение шаблона страницы клиентов с переданными данными о клиентах
    return render(request, "commercial_service/clients.html", {"client": client})


# Функция для создания нового клиента
def create_client(
        request: HttpRequest, # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответа
    
    # Обработка POST-запроса для создания нового клиента
    if request.method == "POST":

        # Создание формы с данными запроса
        form = ClientForm(request.POST)

        # Проверка валидности формы
        if form.is_valid():

            # Сохранение нового клиента в базе данных
            form.save()

            # Получение URL для страницы клиентов
            url = reverse("commercial_service:clients")

            # Перенаправление на страницу клиентов
            return redirect(url)
        
        else:
            
            # Вывод сообщения об ошибке валидации
            print("Данные не валидны")

            # Вывод данных формы для отладки
            print(form.data)
    else:

        # Создание пустой формы при GET-запросе
        form = ClientForm
    
    # Передаем форму в контекст для шаблона
    context = {
        "form": form,
        }
    
    # Отображение шаблона для создания клиента с переданным контекстом
    return render(request, "commercial_service/create-client.html", context = context)
