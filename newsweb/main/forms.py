from dataclasses import fields
from . models import New
from django import forms

class Forma(forms.ModelForm):
    class Meta:
        model = New
        fields = "__all__"
