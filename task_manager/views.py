from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .meta import get_meta
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = "index.html"
    extra_context = {
        'meta': get_meta(),
    }


class MyLoginView(SuccessMessageMixin, LoginView):

    template_name = 'login.html'
    next_page = reverse_lazy('index')
    success_message = get_meta().get('YouAreLogIn')

    extra_context = {
        'meta': get_meta(),
    }


class MyLogoutView(LogoutView):

    next_page = reverse_lazy('index')
    success_message = get_meta().get('YouAreLogOut')
    extra_context = {
        'meta': get_meta(),
    }

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, message=self.success_message)
        return super().dispatch(request, *args, **kwargs)
