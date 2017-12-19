from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Thread, Forum, ForumSection


def index(request):
    return render(
        request,
        'forumapp/index.html'
    )


def forum(request):
    sections = ForumSection.objects.all()
    forums = Forum.objects.all()
    return render(
        request,
        'forumapp/forum.html',
        context={
            'sections': sections,
            # 'forums': forums,
        }
    )
