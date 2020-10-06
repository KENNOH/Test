from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import TimeField
from .models import Asset, Attachments


class DateInput(forms.DateTimeInput):
	input_type = 'date'


class TimeInput(forms.DateTimeInput):
	input_type = 'time'




class AssetForm(forms.ModelForm):
    name = forms.CharField(label='Asset name:', max_length=200, required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}))
    purchase_date = forms.DateField(label='Acquired Date:', required=True, widget=DateInput(attrs={'class': 'form-control form-textbox'}))
    time = forms.TimeField(label='Time:', required=True, widget=TimeInput(attrs={'class': 'form-control form-textbox'}))
    attachment = forms.FileField(label="Attachment:", required=False, widget=forms.ClearableFileInput(attrs={'multiple': "true", 'name': 'attachment'}))
    cost = forms.FloatField(label="Cost in USD:", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Estimated total cost', 'name': 'cost', 'step': "0.01"}))
    description = forms.CharField(label="Description:", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description', 'name': 'description', 'rows': '4'}))

    class Meta:
      model = Asset
      fields = ('name', 'purchase_date', 'time','attachment', 'cost', 'description')
