from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View


class IndexView(View):

    # i18n fields naming

    def get(self, request, *args, **kwargs):

        title = _('Менеджер задач Hexlet')
        project_name = _('Менеджер задач')
        users = _('Пользователи')
        enter = _('Вход')
        registration = _('Регистрация')
        greetings = _('Привет от Хекслета!')
        courses_name = _('Практические курсы по программированию')
        about = _('Узнать больше')
        hexlet = _('Хекслет')

        return render(request, 'index.html', context={
            "title": title,
            "project_name": project_name,
            "users": users,
            "enter": enter,
            "registration": registration,
            "greetings": greetings,
            "courses_name": courses_name,
            "about": about,
            "hexlet": hexlet,
        })
