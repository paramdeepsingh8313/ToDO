from django import forms
from django.forms import ModelForm

from .models import *

class TodoForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs = {'placeholder':'Add new Task..'}))
    class Meta:
        model = Todo
        fields = '__all__'
