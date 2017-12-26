import datetime

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

from forumapp.models import ForumSection, Forum, Thread, ThreadResponse


class ForumSectionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ForumSection.objects.create(
            name="Bugs"
        )

    def test_name_label(self):
        forum_section = ForumSection.objects.get(id=1)
        field_label = forum_section._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length_30(self):
        forum_section = ForumSection.objects.get(id=1)
        name_field = forum_section._meta.get_field('name')
        self.assertEquals(name_field.max_length, 30)

    def test_forum_section_str(self):
        forum_section = ForumSection.objects.get(id=1)
        self.assertEquals(
            str(forum_section),
            'Bugs'
        )


class ForumModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        forum_section = ForumSection.objects.create(
            name="Bugs"
        )

        Forum.objects.create(
            name="My Forum",
            description="My Forum Description",
            section=forum_section
        )

    def test_name_label(self):
        forum = Forum.objects.get(id=1)
        field_label = forum._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        forum = Forum.objects.get(id=1)
        field_label = forum._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_section_label(self):
        forum = Forum.objects.get(id=1)
        field_label = forum._meta.get_field('section').verbose_name
        self.assertEquals(field_label, 'section')

    def test_name_max_length_30(self):
        forum = Forum.objects.get(id=1)
        field_label = forum._meta.get_field('name')
        self.assertEquals(field_label.max_length, 30)

    def test_name_unique(self):
        forum_section = ForumSection.objects.get(id=1)

        with self.assertRaises(IntegrityError):
            Forum.objects.create(
                name="My Forum",
                description="My Forum Description",
                section=forum_section
            )

    def test_description_max_length_200(self):
        forum = Forum.objects.get(id=1)
        description = forum._meta.get_field('description')
        self.assertEquals(description.max_length, 200)

    def test_section_foreign_key(self):
        forum = Forum.objects.get(id=1)
        forum_section = ForumSection.objects.get(id=1)
        self.assertEquals(
            forum.section,
            forum_section
        )

    def test_forum_str(self):
        forum = Forum.objects.get(id=1)
        self.assertEquals(
            str(forum),
            "My Forum"
        )


class ThreadModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        forum = Forum.objects.create(name="My Forum")
        Thread.objects.create(
            name='My Thread',
            forum=forum
        )

    def test_name_field(self):
        thread = Thread.objects.get(pk=1)
        thread_name_field = thread._meta.get_field('name')
        self.assertEquals(thread_name_field.verbose_name, 'name')

    def test_name_field_max_length_100(self):
        thread = Thread.objects.get(pk=1)
        thread_name_field = thread._meta.get_field('name')
        self.assertEquals(
            thread_name_field.max_length,
            100
        )

    def test_forum_association(self):
        forum = Forum.objects.get(id=1)
        thread = Thread.objects.get(id=1)

        self.assertEquals(
            thread.forum,
            forum
        )

    def test_on_delete_forum(self):
        forum = Forum.objects.get(id=1)
        forum.delete()
        thread = Thread.objects.get(id=1)
        self.assertIsNone(
            thread.forum
        )

    def test_thread_str(self):
        thread = Thread.objects.get(id=1)
        self.assertEquals(
            str(thread),
            "My Thread"
        )


class ThreadResponseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        thread = Thread.objects.create(
            name="My Thread"
        )
        user = User.objects.create_user(
            username='jeff'
        )
        ThreadResponse.objects.create(
            thread=thread,
            created_datetime=datetime.datetime.now(),
            responder=user,
            message='My Message'
        )

    def test_thread_association(self):
        thread_response = ThreadResponse.objects.get(id=1)
        thread = Thread.objects.get(id=1)
        self.assertEquals(
            thread_response.thread,
            thread
        )

    def test_user_association(self):
        user = User.objects.get(id=1)
        thread_response = ThreadResponse.objects.get(id=1)
        self.assertEquals(
            thread_response.responder,
            user
        )

    def test_thread_on_delete_thread(self):
        thread = Thread.objects.get(id=1)
        thread.delete()
        thread_response = ThreadResponse.objects.get(id=1)
        self.assertIsNone(
            thread_response.thread
        )

    def test_created_datetime(self):
        thread_response = ThreadResponse.objects.get(id=1)
        self.assertGreater(
            datetime.datetime.now(),
            thread_response.created_datetime.replace(tzinfo=None)
        )

        self.assertLess(
            datetime.datetime.now() + datetime.timedelta(minutes=-5),
            thread_response.created_datetime.replace(tzinfo=None)
        )

    def test_responder_on_delete_user(self):
        user = User.objects.get(id=1)
        user.delete()
        thread_response = ThreadResponse.objects.get(id=1)
        self.assertIsNone(
            thread_response.responder
        )

    def test_message(self):
        thread_response = ThreadResponse.objects.get(id=1)
        self.assertEquals(
            thread_response.message,
            'My Message'
        )

    def test_message_max_length_1000(self):
        thread_response = ThreadResponse.objects.get(id=1)
        thread_response_field = thread_response._meta.get_field('message')
        self.assertEquals(
            thread_response_field.max_length,
            1000
        )

    def test_response_str(self):
        thread_response = ThreadResponse.objects.get(id=1)
        self.assertEquals(
            str(thread_response),
            'My Message'
        )
