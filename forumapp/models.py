from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ForumSection(models.Model):
    name = models.CharField(max_length=30)


class Forum(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    section = models.ForeignKey(
        ForumSection,
        null=True,
        on_delete=models.SET_NULL
    )


class Thread(models.Model):
    name = models.CharField(max_length=100)
    forum = models.ForeignKey(Forum, null=True, on_delete=models.SET_NULL)
    created_date = models.DateField()


class ThreadResponse(models.Model):
    thread = models.ForeignKey(Thread, null=True, on_delete=models.SET_NULL)
    created_date = models.DateField()
    responder = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    message = models.TextField(max_length=1000)
