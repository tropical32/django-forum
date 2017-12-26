from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ForumSection(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Forum(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=200)
    section = models.ForeignKey(
        ForumSection,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Thread(models.Model):
    name = models.CharField(max_length=100)
    forum = models.ForeignKey(Forum, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('can_remove_any_thread', 'Can remove ANY thread.'),
        ]


class ThreadResponse(models.Model):
    thread = models.ForeignKey(Thread, null=True, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(null=True)
    responder = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)

    class Meta:
        permissions = [
            ('can_remove_any_response', 'Can remove ANY response.')
        ]

    def __str__(self):
        return self.message
