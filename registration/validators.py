from django.core.validators import RegexValidator

# Создаем класс PhoneRegexValidator, который наследуется от класса RegexValidator
class PhoneRegexValidator(RegexValidator):
    
    # Устанавливаем регулярное выражение для проверки телефонного номера (10 цифр)
    regex = r"^\d{10}$"
    
    # Устанавливаем сообщение об ошибке, если проверка не прошла
    message = "Телефон должен состоять из 10 цифр"
