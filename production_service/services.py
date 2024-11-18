# Импортируем необходимые классы исключений и модели из Django
from django.core.exceptions import ValidationError
from commercial_service.models import CommercialServiceInfoClientsOfThePlant
from production_service.models import ProductionServiceOrder
from technologist_service.models import TechnologistServiceInfoTypesOfForestProducts

# Эта функция создает новый заказ на производство лесопродукции
def create_order(client_id, product_id, product_quantity, deadline_date):
    try:
        # Получаем клиента и продукт
        client = CommercialServiceInfoClientsOfThePlant.objects.get(id=client_id)
        product = TechnologistServiceInfoTypesOfForestProducts.objects.get(id=product_id)

        # Создаем новый заказ
        order = ProductionServiceOrder(
            client=client,
            product=product,
            product_quantity=product_quantity,
            deadline_date=deadline_date
        )

        # Проверяем валидность заказа
        order.full_clean()

        # Сохраняем заказ
        order.save()

        # Возвращаем созданный заказ и None как ошибку
        return order, None

    except CommercialServiceInfoClientsOfThePlant.DoesNotExist:

        # Обработка случая, когда клиент не найден. Возвращаем None и сообщение об ошибке
        return None, "Клиент не найден."
    
    except TechnologistServiceInfoTypesOfForestProducts.DoesNotExist:
        
        # Обработка случая, когда продукт не найден. Возвращаем None и сообщение об ошибке
        return None, "Продукт не найден."
    
    except ValidationError as e:

        # Обработка исключения ValidationError. Возвращаем None и сообщение об ошибке валидации
        return None, str(e)
    
    except Exception as e:

        # Обработка любых других исключений. Возвращаем None и общее сообщение об ошибке
        return None, f"Ошибка: str(e)"