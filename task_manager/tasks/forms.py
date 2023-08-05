from .models import Task
from django.forms import ModelForm


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['task_name', 'description',
                  'status', 'executor', 'labels']
