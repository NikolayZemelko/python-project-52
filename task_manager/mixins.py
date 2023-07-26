from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from .meta import get_meta


class UserPermissionMixin(UserPassesTestMixin):

    permission_denied_message = get_meta().get('Main').get('NoUpdatingRight')
    permission_url = None

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.permission_url)


class AuthRequiredMixin(LoginRequiredMixin):

    auth_message = get_meta().get('Users').get('NotAuthorised')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_message)
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


class DeleteProtectedMixin:

    protected_url = None
    protected_message = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
