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
        'forum/<int:fpk>/thread/<int:tpk>/respond',
        views.respond,
        name='respond-thread'
    )
    # path(
    #     'forum/<int:fpk>/thread/<int:tpk>/respond',
    #     views.ThreadRespondCreateView.as_view(),
    #     name='respond-thread',
    # )
]
