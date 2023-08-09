from django.contrib.messages.views import SuccessMessageMixin
from task_manager.meta import get_meta
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import SignupForm
from task_manager.mixins import UserPermissionMixin, \
    AuthRequiredMixin, DeleteProtectedMixin


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
    success_message = get_meta().get('Users').get('RegisteredSuccess')


class UserUpdateView(SuccessMessageMixin, AuthRequiredMixin,
                     UserPermissionMixin, UpdateView):

    template_name = 'users/update.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('users-index')
    success_message = get_meta().get('Users').get('UpdatingSuccess')
    permission_denied_message = get_meta().get('Main').get('NoUpdatingRight')
    permission_url = reverse_lazy('users-index')

    extra_context = {
        'meta': get_meta(),
    }


class UserDeleteView(SuccessMessageMixin, AuthRequiredMixin,
                     UserPermissionMixin, DeleteProtectedMixin, DeleteView):

    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users-index')
    success_message = get_meta().get('Users').get('DeletedSuccess')
    permission_denied_message = get_meta().get('Main').get('NoUpdatingRight')
    protected_message = get_meta().get('Users').get('UserInWork')
    permission_url = reverse_lazy('users-index')
    protected_url = reverse_lazy('users-index')
    extra_context = {
        'meta': get_meta(),
    }
