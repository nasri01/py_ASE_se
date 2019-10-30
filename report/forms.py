from django import forms
from acc.models import All_Device
from .models import *

class report_Form(forms.ModelForm):
    class Meta:
        model = report
        fields = '__all__'

