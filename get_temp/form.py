from django import forms
from .models import Thermal


class ThermalPost(forms.ModelForm):
    class Meta:
        model = Thermal
        fields = ['title']
