from django.test import TestCase

from forumapp.models import Forum


class ForumSectionViewTest(TestCase):
    pass


class ForumViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        forum = Forum.objects.create(
            name="My Forum"
        )



