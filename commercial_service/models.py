from django.db import models

# Определяем модель CommercialServiceInfoClientsOfThePlant, которая будет представлять клиентов
class CommercialServiceInfoClientsOfThePlant(models.Model):

    # Настройки метаданных модели
    class Meta:
        
        # Указывает, что Django не будет управлять этой таблицей (не будет создавать/удалять её)
        managed = False

        # Имя таблицы в базе данных
        db_table = 'commercial_service_info_clients_of_the_plant'

        # Имя в единственном числе
        verbose_name = "клиент"

        # Имя во множественном числе
        verbose_name_plural = "клиенты"

    # Определяем поле name, которое будет хранить имя клиента
    name = models.CharField(max_length=100, verbose_name="Клиент")
    
    # Метод str возвращает строковое представление объекта модели
    def __str__(self):

        # Возвращаем имя клиента в качестве строкового представления объекта
        return self.name