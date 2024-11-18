# Импортируем необходимые модули и классы из Django
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from production_service.models import ProductionServiceOrder
from commercial_service.models import CommercialServiceInfoClientsOfThePlant
from technologist_service.models import TechnologistServiceInfoTypesOfForestProducts


# Функция для отображения информации о сервисах
def index_service(
        request: HttpRequest, # Принимаем объект запроса
) -> HttpResponse: # Возвращаем объект ответа
    
    # Получаем все объекты видов лесопродукции
    product = TechnologistServiceInfoTypesOfForestProducts.objects.all()
    
    # Получаем всех клиентов коммерческой службы
    client = CommercialServiceInfoClientsOfThePlant.objects.all()
    
    # Получаем все заказы производственной службы
    order = ProductionServiceOrder.objects.all()

    # Формируем контекст для передачи в шаблон
    context = {
        "product": product,
        "client": client,
        "order": order,
    }

    # Рендерим шаблон с переданным контекстом
    return render(request, "services/index.html", context = context)

