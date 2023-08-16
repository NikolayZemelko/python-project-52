from django_filters import rest_framework as filters, ModelChoiceFilter, BooleanFilter
from .models import Task
from ..labels.models import Label
from django import forms
from ..meta import get_meta


class TaskFilter(filters.FilterSet):

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=get_meta().get('Main').get('Label')
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
