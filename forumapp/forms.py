from django.forms import models, HiddenInput

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
