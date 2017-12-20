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
        views.ThreadListView.as_view(),
        name='forum'
    ),
    path(
        'new-thread/<int:pk>',
        views.CreateThread.as_view(),
        name='new-thread'
    )

]
