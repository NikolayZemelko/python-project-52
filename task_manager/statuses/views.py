from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from task_manager.meta import get_meta
from task_manager.mixins import AuthRequiredMixin
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
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses-index')
    success_message = get_meta().get('Statuses').get('CreatedSuccess')

    extra_context = {
        'meta': get_meta(),
    }


class StatusUpdateView(SuccessMessageMixin, AuthRequiredMixin,
                       UpdateView):

    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses-index')
    success_message = get_meta().get('Statuses').get('UpdatedSuccess')

    extra_context = {
        'meta': get_meta(),
    }


class StatusDeleteView(SuccessMessageMixin, AuthRequiredMixin,
                       DeleteView):

    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses-index')
    success_message = get_meta().get('Statuses').get('DeletedSuccess')

    extra_context = {
        'meta': get_meta(),
    }
