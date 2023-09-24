
from django import forms
from .models import Distros

class DistrosForm(forms.ModelForm):
    class Meta:
        model = Distros
        fields = ['name', 'available']
