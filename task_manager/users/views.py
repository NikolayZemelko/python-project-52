from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from task_manager.mixins import UserPermissionMixin, \
    AuthRequiredMixin, DeleteProtectedMixin
from .forms import SignupForm
from .models import TaskUser


class UsersView(ListView):
    template_name = "users/index.html"
    model = TaskUser
    context_object_name = 'users'


class UsersCreateView(SuccessMessageMixin,
                      CreateView):
    form_class = SignupForm
    template_name = 'form.html'

    extra_context = {
        'title': _('Registration'),
        'button_text': _('Register')
    }

    success_url = reverse_lazy('login')
    success_message = _('User has been '
                        'registered successfully!')


class UserUpdateView(SuccessMessageMixin,
                     AuthRequiredMixin,
                     UserPermissionMixin,
                     UpdateView):
    template_name = 'form.html'
    model = TaskUser
    form_class = SignupForm
    success_url = reverse_lazy('users-index')
    success_message = _('User has been updated successfully!')
    permission_denied_message = _('You do not have rights '
                                  'to change another user.')
    permission_url = reverse_lazy('users-index')

    extra_context = {
        'title': _('Change user'),
        'button_text': _("Change")
    }


class UserDeleteView(SuccessMessageMixin,
                     AuthRequiredMixin,
                     UserPermissionMixin,
                     DeleteProtectedMixin,
                     DeleteView):
    template_name = 'users/delete.html'
    model = TaskUser
    success_url = reverse_lazy('users-index')
    success_message = _("User deleted successfully")
    permission_denied_message = _('You do not have rights '
                                  'to change another user.')
    protected_message = _('Cannot delete user because it is in use')
    permission_url = reverse_lazy('users-index')
    protected_url = reverse_lazy('users-index')
    extra_context = {
        "title": _('Deleting a user'),
        "warning_message": _("Are you sure you want to delete")
    }
