from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_repeat_password(self):
        data = self.cleaned_data

        if data['repeat_password'] != data['password']:
            raise ValidationError("Password didn't match")

        return data['repeat_password']

