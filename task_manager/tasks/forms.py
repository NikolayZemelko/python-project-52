from .models import Task
from ..meta import get_meta
from django.forms import ModelForm


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['task_name', 'description',
                  'status', 'executor', 'labels']
        labels = {
            'task_name': get_meta().get('Main').get('Name'),
            'description': get_meta().get('Main').get('Description'),
            'status': get_meta().get('Statuses').get('Status'),
            'executor': get_meta().get('Users').get('Executor'),
            'labels': get_meta().get('Main').get('Labels')
        }
