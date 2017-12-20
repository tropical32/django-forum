from django.urls import path

from forumapp import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'forums',
        views.forums,
        name='forums'
    ),
    path(
        'forum/<int:pk>',
        # views.ThreadListView.as_view(),
        views.forum,
        name='forum'
    ),
    path(
        'forum/<int:pk>/new-thread',
        # views.ThreadCreateView.as_view(),
        views.new_thread,
        name='new-thread'
    )
]
