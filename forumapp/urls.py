from django.conf.urls import url
from django.urls import path, reverse

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
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>',
        views.thread_view,
        name='thread-view'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/respond/',
        views.respond,
        name='respond-thread'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/delete/',
        views.delete_thread,
        name='thread-delete'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/post/<int:ppk>/edit',
        views.edit_post,
        name='edit-post'
    ),
    # url(
    #     r'^forum/(?P<fpk>[0-9]+)/thread/(?P<tpk>[0-9]+)/respond/$',
    #     views.respond,
    #     name='thread-respond'
    # )
]
