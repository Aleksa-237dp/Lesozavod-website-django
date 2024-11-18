from django.db import models

# Модель для хранения информации о видах лесопродукции
class TechnologistServiceInfoTypesOfForestProducts(models.Model):

    # Настройки метаданных модели
    class Meta:

        # Указывает, что Django не будет управлять этой таблицей (не будет создавать/удалять её)
        
        managed = False

        # Имя таблицы в базе данных
        db_table = 'technologist_service_info_types_of_forest_products'

        # Имя в единственном числе
        verbose_name = "вид лесопродукции"

        # Имя во множественном числе
        verbose_name_plural = "виды лесопродукции"

    # Поле для хранения названия вида лесопродукции
    name = models.CharField(max_length=100,verbose_name="Название вида лесопродукции")
    
    # Поле для хранения описания лесопродукции
    description = models.TextField(verbose_name="Описание лесопродукции")
    
    # Поле для хранения цены за штуку лесопродукции
    price_per_piece = models.DecimalField(max_digits=10, decimal_places=5, verbose_name="Цена за штуку")
    
    # Метод для строкового представления объекта
    def __str__(self):
        return self.name  # Возвращаем название лесопродукции