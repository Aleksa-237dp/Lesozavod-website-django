from django.db import models
from django.core.exceptions import ValidationError
from technologist_service.models import TechnologistServiceInfoTypesOfForestProducts


# Модель для представления заказа на производство лесопродукции
class ProductionServiceOrder(models.Model):

    # Настройки метаданных модели
    class Meta:

        # Указывает, что Django не будет управлять этой таблицей (не будет создавать/удалять её)
        managed = False

        # Имя таблицы в базе данных
        db_table = 'production_service_order'

        # Имя в единственном числе
        verbose_name = "заказ"

        # Имя во множественном числе
        verbose_name_plural = "заказы"

    # Поле для хранения количества лесопродукции в заказе
    product_quantity = models.PositiveIntegerField(verbose_name="Количество лесопродукции (в штуках)", blank=True,)

    # Поле для хранения даты регистрации заказа
    registration_date = models.DateField(verbose_name="Дата регистрации заказа")

    # Поле для хранения даты, к которой требуется выпустить лесопродукцию
    deadline_date = models.DateField(verbose_name="Дата, к которой требуется выпустить лесопродукцию")

    # Поле для хранения дополнительной информации о заказе
    extra_info = models.TextField(verbose_name="Дополнительная информация о заказе")

    # Поле для хранения информации о клиенте-заказчике
    info_client = models.CharField(unique=True, max_length=50, verbose_name="Информация о клиенте-заказчике", blank=True,)

    # Поле для связи с моделью TechnologistServiceInfoTypesOfForestProducts
    product = models.ForeignKey(TechnologistServiceInfoTypesOfForestProducts, on_delete=models.CASCADE, verbose_name="Вид лесопродукции", null=True, blank=True,)
    
    # Определение возможных статусов заказа с использованием списка кортежей
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('approved', 'Согласован клиентом'),
        ('in_production', 'Принят в производство'),
        ('completed', 'Выполнен'),
    ]

    # Поле для хранения статуса заказа
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    # Метод для валидации модели перед сохранением
    def clean(self):

        # Если статус заказа 'approved', то поля info_client, product и product_quantity должны быть заполнены
        if self.status == 'approved':
            if not self.info_client or not self.product or self.product_quantity <= 0:
                raise ValidationError('Для регистрации заказа со статусом "Согласован клиентом" необходимо заполнить информацию о клиенте, виде лесопродукции и количестве.')
    
    # Метод для отображения информации о заказе в строковом представлении
    def __str__(self):
        return f"Заказ от {self.info_client} на {self.product_quantity} единиц(ы) {self.product}"
    