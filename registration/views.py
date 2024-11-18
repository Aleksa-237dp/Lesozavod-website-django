# Импортируем необходимые модули и классы из Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .forms import RegisterForm, ProfileForm
from .models import Profile

# Функция для обработки регистрации нового пользователя
def register(request):

    # Обрабатываем запрос POST для регистрации
    if request.method == "POST":

        # Создаем экземпляр формы регистрации с данными из запроса
        register_form = RegisterForm(request.POST)

        # Создаем экземпляр формы профиля, обрабатывая данные и файлы
        profile_form = ProfileForm(request.POST, request.FILES)

        # Проверяем валидность обеих форм
        if register_form.is_valid() and profile_form.is_valid():

            # Сохраняем пользователя
            user = register_form.save()

            # Создаем профиль, но не сохраняем его сразу
            profile = profile_form.save(commit=False)

            # Связываем профиль с пользователем
            profile.user = user

            # Сохраняем профиль
            profile.save()

            # Авторизуем пользователя
            login(request, user)

            # Выводим сообщение об успешной регистрации
            messages.success(request, "Регистрация прошла успешно!")

            # Перенаправляем на главную страницу (предполагается наличие URL-имени "services:index")
            return redirect("services:index")
        else:

            # Выводим сообщение об ошибках в форме
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        # Создаем пустой экземпляр формы регистрации и профиля
        register_form = RegisterForm()
        profile_form = ProfileForm()

    # Отображаем форму регистрации
    return render(request, "registration/register.html", {"register_form": register_form, "profile_form": profile_form})


# Функция для обработки запроса на страницу профиля пользователя
def profile(request):

    # Получаем текущего пользователя
    user = request.user

    # Получаем или создаем профиль для пользователя
    profile, created = Profile.objects.get_or_create(user=user)

    # Если профиль создан впервые
    if created:

        # Перенаправляем на редактирование профиля
        return redirect('edit-profile')
    
    # Отображаем профиль
    return render(request, "registration/profile.html", {'profile': profile})


# Функция для обработки выхода из системы
def logout_view(request):

    # Выходим из системы
    logout(request)

    # Выводим сообщение о выходе
    messages.success(request, "Вы вышли из системы.")

    # Перенаправляем на страницу входа
    return redirect("registration:login")


# Функция для обработки входа в систему
def login_view(request):
    
    if request.method == "POST":

        # Создаем экземпляр формы аутентификации с данными из запроса
        form = AuthenticationForm(data=request.POST)

        # Проверяем валидность формы
        if form.is_valid():

            # Получаем пользователя
            user = form.get_user()

            # Авторизуем пользователя
            login(request, user)

            # Выводим сообщение об успешном входе
            messages.success(request, "Вы успешно вошли в систему.")

            # Перенаправляем на главную страницу
            return redirect(reverse("services:index"))
        else:
            # Выводим сообщение об ошибке
            messages.error(request, "Неверный логин или пароль.")
    else:

        # Создаем пустой экземпляр формы аутентификации
        form = AuthenticationForm()

    # Отображаем форму входа
    return render(request, "registration/login.html", context={"form": form})