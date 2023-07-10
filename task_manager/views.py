from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def get_meta():

    return dict(
            Title=_('Менеджер задач Hexlet'),
            Project_name=_('Менеджер задач'),
            Users=_('Пользователи'),
            Enter=_('Вход'),
            Registration=_('Регистрация'),
            Greetings=_('Привет от Хекслета!'),
            Courses_name=_('Практические курсы по программированию'),
            About=_('Узнать больше'),
            Hexlet=_('Хекслет'),
            Id=_('ID'),
            UserName=_('Имя пользователя'),
            FullName=_('Полное имя'),
            DateOfCreate=_('Дата создания'),
            Name=_('Имя'),
            LastName=_('Фамилия'),
            RequirmentField=_('Обязательное поле. Не более 150 символов.'
                              ' Только буквы, цифры и символы'),
            Password=_('Пароль'),
            PasswordRequirment=_('Ваш пароль должен содержать как минимум 3 символа.'),
            PasswordApproval=_('Подтверждение пароля'),
            PasswordApprovalAgain=_('Для подтверждения введите, пожалуйста, пароль ещё раз.'),
            Register=_('Зарегистрировать'),
        )


class IndexView(View):

    # i18n fields naming

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html', context={
            'meta': get_meta(),
        })


class UsersView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'users/index.html', context={
            'meta': get_meta(),
        })


class UsersCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/create.html', context={
            'meta': get_meta(),
        })

    def post(self, request, *args, **kwargs):
        ...


class UserUpdateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'user/update.html', context={
            'meta': get_meta(),
        })

    def post(self, request, *args, **kwargs):
        ...


class UserDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'user/delete.html', context={
            'meta': get_meta(),
        })

    def post(self, request, *args, **kwargs):
        ...


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/login.html', context={
            'meta': get_meta(),
        })

    def post(self, request, *args, **kwargs):
        ...


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        ...
