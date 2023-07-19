from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from task_manager.forms import SignupForm


def get_meta():

    return dict(
            Title=_('Менеджер задач Hexlet'),
            Project_name=_('Менеджер задач'),
            Users=_('Пользователи'),
            EnterHeader=_('Вход'),
            Entering=_('Войти'),
            LogOut=_('Выход'),
            Registration=_('Регистрация'),
            Updating=_('Изменение пользователя'),
            Greetings=_('Привет от Хекслета!'),
            Courses_name=_('Практические курсы по программированию'),
            About=_('Узнать больше'),
            Hexlet=_('Hexlet'),
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
            UpdateUser=_('Изменить'),
            DeleteUser=_('Удалить'),
            DeletingUser=_('Удаление пользователя'),
            DeletingApproving=_('Вы уверены, что хотите удалить'),
            Statuses=_('Статусы'),
            Labels=_('Метки'),
            Tasks=_('Задачи'),
        )


class IndexView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html', context={
            'meta': get_meta(),
        })


class UsersView(View):

    def get(self, request, *args, **kwargs):

        users = User.objects.all()

        return render(request, 'users/index.html', context={
            'meta': get_meta(),
            'users': users,
        })


class UsersCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/create.html', context={
            'meta': get_meta(),
        })

    def post(self, request, *args, **kwargs):

        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.clean_username()

            if User.objects.filter(username=username):
                messages.add_message(request, messages.ERROR,
                                     _('Пользователь с таким именем уже существует.'))
                return redirect('users-create', {
                    'form': form,
                })

            else:

                user = form.save()
                login(request, user)
                messages.add_message(request, messages.SUCCESS,
                                     _('Пользователь успешно зарегистрирован'))
                return redirect(settings.LOGIN_REDIRECT_URL)

        else:
            messages.add_message(request, messages.ERROR,
                                 _('Неправильные значения, попробуйте снова.'))

            return redirect('users-create')


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


class MyLoginView(LoginView):

    template_name = 'users/login.html'
    next_page = reverse_lazy('index')

    extra_context = {
        'meta': get_meta(),
    }

    def form_valid(self, form):
        messages.success(self.request, _('Вы залогинены'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Ошибка входа.'))
        return super().form_invalid(form)


class MyLogoutView(LogoutView):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(self.request, _('Вы разлогинены'))
        return redirect('index')
