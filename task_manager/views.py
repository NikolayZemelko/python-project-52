from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View


class IndexView(View):

    # i18n fields naming

    def get(self, request, *args, **kwargs):

        meta = dict(
            Title=_('Менеджер задач Hexlet'),
            Project_name=_('Менеджер задач'),
            Users=_('Пользователи'),
            Enter=_('Вход'),
            Registration=_('Регистрация'),
            Greetings=_('Привет от Хекслета!'),
            Courses_name=_('Практические курсы по программированию'),
            About=_('Узнать больше'),
            Hexlet=_('Хекслет'),
        )
        print(meta)
        return render(request, 'index.html', context={
            'meta': meta,
        })


class UsersView(View):

    def get(self, request, *args, **kwargs):

        meta = dict(
            Id=_('ID'),
            UserName=_('Имя пользователя'),
            FullName=_('Полное имя'),
            DateOfCreate=_('Дата создания'),
        )
        return render(request, 'users/index.html', context={
            'meta': meta,
        })
