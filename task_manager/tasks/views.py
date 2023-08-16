from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from django.views.generic import (UpdateView, DeleteView,
                                  CreateView, DetailView)
from django.urls import reverse_lazy
from django_filters.views import FilterView
from task_manager.meta import get_meta
from .models import Task
from ..users.models import TaskUser
from .forms import TaskForm
from .filters import TaskFilter


class TaskView(DetailView):

    template_name = "tasks/task.html"
    model = Task

    extra_context = {
        'meta': get_meta(),
    }


class TasksView(AuthRequiredMixin, FilterView):

    template_name = "tasks/index.html"
    model = Task
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    extra_context = {
        'meta': get_meta(),
        'users': User.objects.only('first_name', 'last_name'),
        'labels': Label.objects.only('label_name'),
        'statuses': Status.objects.only('status_name')
    }


class TasksCreateView(SuccessMessageMixin, CreateView):

    form_class = TaskForm
    template_name = 'tasks/create.html'

    extra_context = {
        'meta': get_meta(),
    }

    success_url = reverse_lazy('tasks-index')
    success_message = get_meta().get('Tasks').get('CreatedSuccess')

    def form_valid(self, form):

        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)

        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):

    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks-index')
    success_message = get_meta().get('Tasks').get('UpdatedSuccess')

    extra_context = {
        'meta': get_meta(),
    }


class TaskDeleteView(SuccessMessageMixin, AuthRequiredMixin,
                     AuthorDeletionMixin, DeleteView):

    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks-index')
    success_message = get_meta().get('Tasks').get('DeletedSuccess')
    author_message = get_meta().get(
        'Tasks').get(
        'OnlyAuthorCanDel')
    author_url = reverse_lazy('tasks-index')
    extra_context = {
        'meta': get_meta(),
    }
