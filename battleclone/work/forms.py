from django import forms
from django.forms.widgets import Select
from .models import Work


class WorkModelForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['work_type']
        widgets = {
            'work_type': Select
        }
