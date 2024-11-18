import logging
from django.contrib.contenttypes.models import ContentType
from lesozavod.models import Order
from commercial_service.models import Client, Forest_products
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ObjectDoesNotExist

# Настройка логирования
logger = logging.getLogger(__name__)

def assign_permissions():
    try:
        # Получаем группы
        commercial_group = Group.objects.get(name='Commercial Staff')
        production_group = Group.objects.get(name='Production Staff')
        tech_group = Group.objects.get(name='Tech Staff')

        # Получаем ContentType для моделей
        product_content_type = ContentType.objects.get_for_model(Forest_products)
        client_content_type = ContentType.objects.get_for_model(Client)
        order_content_type = ContentType.objects.get_for_model(Order)

        # Определяем коды разрешений
        commercial_permissions_codenames = [
            'add_Forest_products',
            'change_Forest_products',
            'view_Forest_products',
            'add_Client',
            'change_Client',
            'view_Client',
            'add_order',
            'change_order',
            'view_order',
        ]

        # Получаем разрешения
        commercial_permissions = []
        for codename in commercial_permissions_codenames:
            try:
                permission = Permission.objects.get(codename=codename, content_type__in=[product_content_type, client_content_type, order_content_type])
                commercial_permissions.append(permission)
            except ObjectDoesNotExist:
                logger.warning(f"Permission 'codename' does not exist.")

        # Добавляем разрешения в группу
        for perm in commercial_permissions:
            commercial_group.permissions.add(perm)

        logger.info(f"Permissions assigned to commercial_group.name successfully.")

    except ObjectDoesNotExist as e:
        logger.error(f"Error: str(e) - Check if the group or permission exists.")