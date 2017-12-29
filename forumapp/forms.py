from django.forms import models
from django.urls import reverse
from django.views.generic import DeleteView

from .models import Thread, ThreadResponse, LikeDislike


class ThreadCreateModelForm(models.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        # widgets = {'forum': HiddenInput()}


class ThreadResponseModelForm(models.ModelForm):
    class Meta:
        model = ThreadResponse
        fields = ['message']


class ThreadDeleteForm(models.ModelForm):
    class Meta:
        model = Thread
        fields = []


class ThreadResponseDeleteForm(models.ModelForm):
    class Meta:
        model = Thread
        fields = []


class LikeDislikeForm(models.ModelForm):
    class Meta:
        model = LikeDislike
        fields = []
