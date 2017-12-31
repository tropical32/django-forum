from django import template

register = template.Library()


@register.filter(name='can_remove_response')
def can_remove_response(response, user):
    return user == response.responder or \
           user.has_perm('forumapp.can_remove_any_response')


@register.filter(name='times0')
def times0(count):
    return ''.join([str(num) for num in range(count)])


@register.filter(name='times')
def times(count):
    return ''.join([str(num) for num in range(1, count + 1)])


@register.filter(name='summarize_likes')
def summarize_likes(likes_dislikes):
    likes = likes_dislikes.filter(like=True).count()
    dislikes = likes_dislikes.filter(like=False).count()

    return likes - dislikes


@register.filter(name='capitalize')
def capitalize(text):
    return text.upper()
