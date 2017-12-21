from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import models, HiddenInput, forms

from .models import Thread, ThreadResponse


class ThreadCreateModelForm(models.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        # widgets = {'forum': HiddenInput()}


class ThreadResponseModelForm(models.ModelForm):
    class Meta:
        model = ThreadResponse
        fields = ['message']
