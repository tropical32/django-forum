from django import template

register = template.Library()


@register.filter(name='can_remove_response')
def can_remove_response(response, user):
    return user == response.responder or \
           user.has_perm('forumapp.can_remove_any_response')
