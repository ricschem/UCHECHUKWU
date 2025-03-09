# forms.py
from django import forms
from .models import EjecsModel


class JolpecForm(forms.ModelForm):

    class Meta:
        model = EjecsModel
        fields = ['title', 'description', 'logo']