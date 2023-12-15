from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class UserPermissionMixin(UserPassesTestMixin):

    permission_denied_message = None
    permission_url = None

    def test_func(self):
        return str(self.get_object().username) == str(self.request.user)

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.permission_url)


class AuthRequiredMixin(LoginRequiredMixin):

    auth_message = _("You are not authorized! Please sign in.")

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


class AuthorDeletionMixin(UserPassesTestMixin):

    author_message = None
    author_url = None

    def test_func(self):
        return str(self.get_object().author.username) == str(self.request.user)

    def handle_no_permission(self):
        messages.error(self.request, self.author_message)
        return redirect(self.author_url)
