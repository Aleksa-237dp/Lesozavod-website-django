# Импортируем необходимые модули и классы из Django
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ProductionServiceOrder
from .forms import OrderForm
import json

# Функция для создания заказа
def production(
        request: HttpRequest # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответ
    
    # Отображаем шаблон "production.html" для страницы создания заказа
    return render(request, "production_service/production.html")


# Функция принимает объект запроса и возвращает объект ответа
# Она отображает список заказов. Доступ ограничен авторизованными пользователями
@login_required
def orders(
        request: HttpRequest, # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответа
        
        # Получаем все заказы из базы данных, используя select_related для оптимизации запроса.
        order = ProductionServiceOrder.objects.select_related('product').all()
        
        # Передаем форму в контекст для шаблона
        context = {
            "order": order,
        }
    
        # Отображаем шаблон "orders.html" для страницы технолога
        return render(request, "production_service/orders.html", context = context)

# Функция для обработки регистрации нового заказа
# Она принимает POST-запросы для сохранения данных
def register_order(
        request: HttpRequest
) -> HttpResponse:
    
    # Проверяем, был ли отправлен POST-запрос
    if request.method == "POST":

        # Создаем форму с данными из запроса
        form = OrderForm(request.POST)
        
        # Проверяем, валидна ли форма
        if form.is_valid():

            # Сохраняем данные формы, но не сохраняем в базу данных пока
            order = form.save(commit=False)

            # Проверка статуса заказа и обязательных полей
            if order.status == 'approved':

                if not order.info_client or not order.product or not order.product_quantity:

                    # Добавляем ошибку в форму, если не указаны необходимые поля
                    form.add_error(None, 'Необходимо заполнить информацию о клиенте, виде лесопродукции и количестве.')
                    
                    # Здесь возможно стоит вернуть форму с ошибкой пользователю, а не печатать в консоль
                    return render(request, "production_service/register_order.html", {'form': form})

            # Устанавливаем флаг, что заказ отправлен
            order.is_submitted = True

            # Сохраняем заказ в базу данных
            order.save()

            # Сохраняем форму
            form.save()
            
            # Получаем URL для перенаправления
            url = reverse("production_service:orders")

            # Перенаправляем на страницу со списком заказов
            return redirect(url)
            
            
        else:

            # Выводим сообщение об ошибке
            print("Данные не валидны")

            # Выводим данные формы для отладки
            print(form.data)
    else:
        # Если не POST-запрос, создаем пустую форму
        form = OrderForm
        
    # Отображаем шаблон с формой
    return render(request, "production_service/register_order.html", {'form': form})

# Декоратор отключает проверку CSRF. Используйте с осторожностью! В продакшене лучше использовать другой подход, например, проверку подписи
@csrf_exempt

# Функция обновляет статус заказа и принимает POST-запросы с JSON-данными
def update_order_status(request, order_id):
    if request.method == 'POST':

        # Получаем JSON-данные из тела запроса
        data = json.loads(request.body)

        # Получаем новый статус из JSON-данных
        new_status = data.get('status')

        try:

            # Поиск заказа по ID. Важно: OrderForm здесь кажется некорректным. Используйте модель Order
            order = OrderForm.objects.get(id=order_id)

            # Устанавливаем новый статус заказа
            order.status = new_status

            # Сохраняем изменения в базе данных
            order.save()

            # Возвращаем JSON-ответ об успехе
            return JsonResponse({'status': 'success'})
        
        # Обработка исключения, если заказ не найден
        except OrderForm.DoesNotExist:

            # Возвращаем JSON-ответ об ошибке (404 Not Found)
            return JsonResponse({'status': 'error', 'message': 'Order not found'}, status=404)
    
    # Возвращаем JSON-ответ об ошибке (400 Bad Request)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)