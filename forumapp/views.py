from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Thread, Forum, ForumSection


def index(request):
    return render(
        request,
        'forumapp/index.html'
    )


def forums(request):
    sections = ForumSection.objects.all()
    forums = Forum.objects.all()
    return render(
        request,
        'forumapp/forums.html',
        context={
            'sections': sections,
            # 'forums': forums,
        }
    )


class ThreadListView(ListView):
    model = Thread


class CreateThread(CreateView):
    model = Thread
