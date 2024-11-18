from django.db import models
from django.contrib.auth.models import User
from .validators import PhoneRegexValidator
from django.core.exceptions import ValidationError


# Модель для хранения профиля пользователя
class Profile(models.Model):

    # Настройки метаданных модели
    class Meta:

        # Имя в единственном числе
        verbose_name = "профиль"

        # Имя во множественном числе
        verbose_name_plural = "профили"
        
    # Определяем роли пользователей с помощью TextChoices
    class Role(models.TextChoices):

        COMMERCIAL_EMPLOYEE = "commercial_employee", "Сотрудник коммерческой службы"
        PRODUCTION_EMPLOYEE = "production_employee", "Сотрудник службы производства"
        TECHNICAL_EMPLOYEE = "technical_employee", "Сотрудник службы технолога"
        CLIENT = "client", "Клиент"

    # Поле для хранения роли пользователя с выбором из перечисленных ролей
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.COMMERCIAL_EMPLOYEE,
        verbose_name="Роль пользователя",
    )

    # Связываем профиль с пользователем (один к одному)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    # Поле для загрузки аватара пользователя
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Аватар (фото)")
    
    # Поле для хранения номера телефона с валидатором
    phone = models.CharField(
        max_length = 10,
        validators = [PhoneRegexValidator()],
        blank = True,
        verbose_name = "Номер телефона",
    )

    # Поле для хранения дополнительной информации о пользователе
    extra_info = models.TextField(
        blank = True,
        verbose_name = "Доп. информация",
    )

    # Метод для строкового представления объекта Profile
    def __str__(self):
        return self.user.username # Возвращаем имя пользователя как строковое представление