from django.contrib.messages.views import SuccessMessageMixin
from task_manager.meta import get_meta
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from .models import TaskUser
from django.urls import reverse_lazy
from .forms import SignupForm
from task_manager.mixins import UserPermissionMixin, \
    AuthRequiredMixin, DeleteProtectedMixin


class UsersView(ListView):

    template_name = "users/index.html"
    model = TaskUser
    context_object_name = 'users'
    extra_context = {
        'meta': get_meta(),
    }


class UsersCreateView(SuccessMessageMixin, CreateView):

    form_class = SignupForm
    template_name = 'form.html'

    extra_context = {
        'meta': get_meta(),
        'title': get_meta().get('Main').get('Registration'),
        'button_text': get_meta().get('Main').get('Register')
    }

    success_url = reverse_lazy('login')
    success_message = get_meta().get('Users').get('RegisteredSuccess')


class UserUpdateView(SuccessMessageMixin, AuthRequiredMixin,
                     UserPermissionMixin, UpdateView):

    template_name = 'form.html'
    model = TaskUser
    form_class = SignupForm
    success_url = reverse_lazy('users-index')
    success_message = get_meta().get('Users').get('UpdatingSuccess')
    permission_denied_message = get_meta().get('Main').get('NoUpdatingRight')
    permission_url = reverse_lazy('users-index')

    extra_context = {
        'meta': get_meta(),
        'title': get_meta().get('Users').get('Updating'),
        'button_text': get_meta().get('Main').get('Update')
    }


class UserDeleteView(SuccessMessageMixin, AuthRequiredMixin,
                     UserPermissionMixin, DeleteProtectedMixin, DeleteView):

    template_name = 'users/delete.html'
    model = TaskUser
    success_url = reverse_lazy('users-index')
    success_message = get_meta().get('Users').get('DeletedSuccess')
    permission_denied_message = get_meta().get('Main').get('NoUpdatingRight')
    protected_message = get_meta().get('Users').get('UserInWork')
    permission_url = reverse_lazy('users-index')
    protected_url = reverse_lazy('users-index')
    extra_context = {
        'meta': get_meta(),
    }
