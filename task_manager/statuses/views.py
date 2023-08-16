from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from task_manager.meta import get_meta
from task_manager.mixins import AuthRequiredMixin, DeleteProtectedMixin
from .forms import StatusForm
from .models import Status


class StatusesView(ListView):

    template_name = "statuses/index.html"
    model = Status
    context_object_name = 'statuses'
    extra_context = {
        'meta': get_meta(),
    }


class StatusesCreateView(SuccessMessageMixin, AuthRequiredMixin,
                         CreateView):

    form_class = StatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('statuses-index')
    success_message = get_meta().get('Statuses').get('CreatedSuccess')

    extra_context = {
        'meta': get_meta(),
        'title': get_meta().get('Statuses').get('CreateStatus'),
        'button_text': get_meta().get('Main').get('CreateButton')
    }


class StatusUpdateView(SuccessMessageMixin, AuthRequiredMixin,
                       UpdateView):

    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses-index')
    success_message = get_meta().get('Statuses').get('UpdatedSuccess')

    extra_context = {
        'meta': get_meta(),
        'title': get_meta().get('Statuses').get('UpdateStatus'),
        'button_text': get_meta().get('Main').get('Update')
    }


class StatusDeleteView(SuccessMessageMixin, AuthRequiredMixin,
                       DeleteProtectedMixin, DeleteView):

    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses-index')
    success_message = get_meta().get('Statuses').get('DeletedSuccess')
    protected_message = get_meta().get('Statuses').get('StatusInWork')
    protected_url = reverse_lazy('statuses-index')
    extra_context = {
        'meta': get_meta(),
    }
