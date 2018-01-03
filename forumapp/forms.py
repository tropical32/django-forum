from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import models, CharField, TextInput, PasswordInput
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


class StylizedUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(StylizedUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(
            attrs={'class': 'form-control'}
        )
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control'}
        )
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control'}
        )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields


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
