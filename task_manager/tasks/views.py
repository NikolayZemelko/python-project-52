from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (UpdateView, DeleteView,
                                  CreateView, DetailView)
from django_filters.views import FilterView

from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from .filters import TaskFilter
from .forms import TaskForm
from .models import Task
from ..users.models import TaskUser


class TaskView(DetailView):
    template_name = "tasks/task.html"
    model = Task


class TasksView(AuthRequiredMixin,
                FilterView):
    template_name = "tasks/index.html"
    model = Task
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TasksCreateView(SuccessMessageMixin,
                      CreateView):
    form_class = TaskForm
    template_name = 'form.html'

    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create')
    }

    success_url = reverse_lazy('tasks-index')
    success_message = _('Task created successfully')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = TaskUser.objects.get(pk=user.pk)

        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin,
                     AuthRequiredMixin,
                     UpdateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks-index')
    success_message = _('Task changed successfully')

    extra_context = {
        'title': _('Create task'),
        'button_text': _('Change')
    }


class TaskDeleteView(SuccessMessageMixin,
                     AuthRequiredMixin,
                     AuthorDeletionMixin,
                     DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks-index')
    success_message = _('Task deleted successfully')
    author_message = _('A task can only be '
                       'deleted by its author.')
    author_url = reverse_lazy('tasks-index')

    extra_context = {
        "title": _('Delete task'),
        "warning_message": _("Are you sure you want to delete")
    }
