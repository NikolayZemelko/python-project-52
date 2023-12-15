from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from task_manager.mixins import AuthRequiredMixin, DeleteProtectedMixin
from .forms import LabelForm
from .models import Label


class LabelsView(ListView):
    template_name = "labels/index.html"
    model = Label
    context_object_name = 'labels'


class LabelsCreateView(SuccessMessageMixin,
                       AuthRequiredMixin,
                       CreateView):
    form_class = LabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('labels-index')
    success_message = _('Label created successfully')

    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create')
    }


class LabelUpdateView(SuccessMessageMixin,
                      AuthRequiredMixin,
                      UpdateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels-index')
    success_message = _('Label changed successfully')

    extra_context = {
        'title': _('Update label'),
        'button_text': _('Change')
    }


class LabelDeleteView(SuccessMessageMixin,
                      AuthRequiredMixin,
                      DeleteProtectedMixin,
                      DeleteView):
    template_name = 'labels/delete.html'
    model = Label
    success_url = reverse_lazy('labels-index')
    success_message = _('Label deleted successfully')
    protected_message = _("Can't delete label because it's in use")
    protected_url = reverse_lazy('labels-index')
    extra_context = {
        "title": _('Delete label'),
        "warning_message": _("Are you sure you want to delete")
    }
