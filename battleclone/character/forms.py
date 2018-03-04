from django.forms import inlineformset_factory
from django import forms
from . import models


class CharacterModelForm(forms.ModelForm):
    class Meta:
        model = models.Character
        fields = '__all__'



