from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['label_name']
        labels = {
            'label_name': _('Name')
        }
