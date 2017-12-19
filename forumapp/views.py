from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(
        request,
        'forumapp/index.html'
    )


def forum(request):
    return render(
        request,
        'forumapp/forum.html'
    )
