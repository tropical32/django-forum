from django.forms import models, CharField, TextInput
from django import forms
from .models import Thread, ThreadResponse, LikeDislike, ForumUser


class ThreadCreateModelForm(models.ModelForm):
    class Meta:
        model = Thread
        fields = ['name', 'forum']
        # widgets = {'forum': HiddenInput()}
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'forum': forms.Select(attrs={'class': 'form-control'}),
        }


class ThreadResponseModelForm(models.ModelForm):
    class Meta:
        model = ThreadResponse
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }


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


class BanUserForm(models.ModelForm):
    class Meta:
        model = ForumUser
        # fields = ['username']
        fields = ['banned_until']


class PinThreadForm(models.ModelForm):
    class Meta:
        model = Thread
        fields = ['pinned']
