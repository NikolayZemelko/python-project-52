from .models import Label
from ..meta import get_meta
from django.forms import ModelForm


class LabelForm(ModelForm):

    class Meta:
        model = Label
        fields = ['label_name']
        labels = {
            'label_name': get_meta().get('Main').get('Name')
        }
