from django import forms
from django.utils.translation import gettext_lazy as _
from django_filters import (rest_framework as filters,
                            ModelChoiceFilter, BooleanFilter)

from .models import Task
from ..labels.models import Label
from ..statuses.models import Status
from ..users.models import TaskUser


class TaskFilter(filters.FilterSet):
    status = ModelChoiceFilter(
        queryset=Status.objects.only('status_name'),
        label=_('Status')
    )

    executor = ModelChoiceFilter(
        queryset=TaskUser.objects.only('username'),
        label=_('Executor')
    )

    labels = ModelChoiceFilter(
        queryset=Label.objects.only('label_name'),
        label=_('Label')
    )

    own_tasks = BooleanFilter(
        label=_('Only your tasks'),
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
