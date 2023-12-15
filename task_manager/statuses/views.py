from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from task_manager.mixins import AuthRequiredMixin, DeleteProtectedMixin
from .forms import StatusForm
from .models import Status


class StatusesView(ListView):
    template_name = "statuses/index.html"
    model = Status
    context_object_name = 'statuses'


class StatusesCreateView(SuccessMessageMixin,
                         AuthRequiredMixin,
                         CreateView):
    form_class = StatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('statuses-index')
    success_message = _('Status created successfully')

    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create')
    }


class StatusUpdateView(SuccessMessageMixin,
                       AuthRequiredMixin,
                       UpdateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses-index')
    success_message = _('Status has been updated successfully!')

    extra_context = {
        'title': _('Change status'),
        'button_text': _('Change')
    }


class StatusDeleteView(SuccessMessageMixin,
                       AuthRequiredMixin,
                       DeleteProtectedMixin,
                       DeleteView):
    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses-index')
    success_message = _("Status deleted successfully")
    protected_message = _("Can't delete status because it's in use")
    protected_url = reverse_lazy('statuses-index')

    extra_context = {
        "title": _('Delete status'),
        "warning_message": _("Are you sure you want to delete")
    }
