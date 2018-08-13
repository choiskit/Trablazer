from django import forms
from django.forms import ModelForm
from .models import IDCInfo 


class IDCInfoForm(ModelForm):
    class Meta:
        model = IDCInfo
	fields = '__all__'
