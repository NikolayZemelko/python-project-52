from django_filters import (rest_framework as filters,
                            ModelChoiceFilter, BooleanFilter)
from .models import Task
from ..labels.models import Label
from ..statuses.models import Status
from ..users.models import TaskUser
from django import forms
from ..meta import get_meta


class TaskFilter(filters.FilterSet):

    status = ModelChoiceFilter(
        queryset=Status.objects.only('status_name'),
        label=get_meta().get('Statuses').get('Status')
    )

    executor = ModelChoiceFilter(
        queryset=TaskUser.objects.only('username'),
        label=get_meta().get('Users').get('Executor')
    )

    labels = ModelChoiceFilter(
        queryset=Label.objects.only('label_name'),
        label=get_meta().get('Labels').get('Label')
    )

    own_tasks = BooleanFilter(
        label=get_meta().get('Tasks').get('OnlyYourTasks'),
        widget=forms.CheckboxInput,
        method='get_own_tasks',
    )

    def get_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor']
