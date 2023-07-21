from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.forms import SignupForm


def get_meta():

    return dict(
            Title=_('Hexlet Task Manager'),
            Project_name=_('Task Manager'),
            Users=_('Users'),
            EnterHeader=_('Log in'),
            Entering=_('Sigh in'),
            LogOut=_('Log Out'),
            YouAreLogIn=_('You are logged in'),
            YouAreLogOut=_('You are logged out'),
            Registration=_('Registration'),
            RegisteredSuccessfully=_('User has been registered successfully!'),
            UpdatingSuccessfully=_('User has been updated successfully!'),
            DelitedSuccessfully=_("User deleted successfully"),
            DeleteButton=_('Yes, delete'),
            NotAuthorised=_("You are not authorized! Please sign in."),
            Updating=_('Change user'),
            Greetings=_('Hello from Hexlet!'),
            Courses_name=_('Practical programming courses'),
            About=_('Learn more'),
            Hexlet=_('Hexlet'),
            Id=_('ID'),
            UserName=_('Username'),
            FullName=_('Fullname'),
            DateOfCreate=_('Date of creation'),
            FirstName=_('Firstname'),
            LastName=_('Lastname'),
            RequirmentField=_('Obligatory field. No more than 150 characters. '
                              'Only letters, numbers and symbols'),
            Password=_('Password'),
            PasswordRequirment=_('Your password must contain at least 3 characters.'),
            PasswordApproval=_('Password confirmation'),
            PasswordApprovalAgain=_('To confirm, please enter your password again.'),
            Register=_('Register'),
            UpdateUser=_('Change'),
            DeleteUser=_('Delete'),
            DeletingUser=_('Deleting a user'),
            DeletingApproving=_('Are you sure you want to delete'),
            Statuses=_('Statuses'),
            Labels=_('Labels'),
            Tasks=_('Tasks'),
        )


class IndexView(TemplateView):

    template_name = "index.html"
    extra_context = {
        'meta': get_meta(),
    }


class UsersView(ListView):

    template_name = "users/index.html"
    model = User
    context_object_name = 'users'
    extra_context = {
        'meta': get_meta(),
    }


class UsersCreateView(SuccessMessageMixin, CreateView):

    form_class = SignupForm
    template_name = 'users/create.html'

    extra_context = {
        'meta': get_meta(),
    }

    success_url = reverse_lazy('login')
    success_message = get_meta().get('RegisteredSuccessfully')


class UserUpdateView(SuccessMessageMixin,
                     LoginRequiredMixin, UpdateView):

    template_name = 'users/update.html'
    model = User
    form_class = SignupForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')
    permission_denied_message = get_meta().get('NotAuthorised')
    extra_context = {
        'meta': get_meta(),
    }


class UserDeleteView(DeleteView):

    model = User
    success_url = 'login'

    def get(self, request, *args, **kwargs):

        user = User.objects.get(id=kwargs['pk'])
        username = user.username

        meta = dict(get_meta())
        deleting_user = meta.get('DeletingApproving')
        meta['DeletingApproving'] = _(f'{deleting_user} {username}?')

        return render(request, 'users/delete.html', context={
            'meta': meta,
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
        return super().form_invalid(form)


class MyLogoutView(LogoutView):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(self.request, _('Вы разлогинены'))
        return redirect('index')
