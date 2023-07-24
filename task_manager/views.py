from django.contrib.messages.views import SuccessMessageMixin
from .meta import get_meta
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.forms import SignupForm
from task_manager.mixins import UserPermissionMixin, AuthRequiredMixin, DeleteProtectedMixin


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
    success_url = reverse_lazy('users')

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            messages.error(self.request, message=get_meta().get('NotAuthorised'))
            return redirect('login')

        user = User.objects.get(id=kwargs['pk'])

        return render(request, 'users/delete.html', context={
            'meta': get_meta(),
            'user': user,
        })

    def form_valid(self, form):
        messages.success(self.request, message=get_meta().get('DeletedSuccessfully'))
        return super().form_valid(form)


class MyLoginView(LoginView):

    template_name = 'users/login.html'
    next_page = reverse_lazy('index')

    extra_context = {
        'meta': get_meta(),
    }

    def form_valid(self, form):
        messages.success(self.request, message=get_meta().get('YouAreLogIn'))
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class MyLogoutView(LogoutView):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(self.request, message=get_meta().get('YouAreLogOut'))
        return redirect('index')
