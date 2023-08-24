from task_manager.statuses.models import Status
from django.forms import ModelForm
from ..meta import get_meta


class StatusForm(ModelForm):

    class Meta:
        model = Status
        fields = ['status_name']
        labels = {
            'status_name': get_meta().get('Main').get('Name')
        }
