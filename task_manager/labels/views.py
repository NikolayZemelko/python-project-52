from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from task_manager.meta import get_meta
from task_manager.mixins import AuthRequiredMixin, DeleteProtectedMixin
from .forms import LabelForm
from .models import Label


class LabelsView(ListView):
    template_name = "labels/index.html"
    model = Label
    context_object_name = 'labels'
    extra_context = {
        'meta': get_meta(),
    }


class LabelsCreateView(SuccessMessageMixin, AuthRequiredMixin,
                       CreateView):

    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels-index')
    success_message = get_meta().get('Labels').get('CreatedSuccess')

    extra_context = {
        'meta': get_meta(),
    }


class LabelUpdateView(SuccessMessageMixin, AuthRequiredMixin,
                      UpdateView):

    template_name = 'labels/update.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels-index')
    success_message = get_meta().get('Labels').get('UpdatedSuccess')

    extra_context = {
        'meta': get_meta(),
    }


class LabelDeleteView(SuccessMessageMixin, AuthRequiredMixin,
                      DeleteProtectedMixin, DeleteView):

    template_name = 'labels/delete.html'
    model = Label
    success_url = reverse_lazy('labels-index')
    success_message = get_meta().get('Labels').get('DeletedSuccess')
    protected_message = get_meta().get('Labels').get('LabelInWork')
    protected_url = reverse_lazy('labels-index')
    extra_context = {
        'meta': get_meta(),
    }
