from django.contrib import admin

# Register your models here.
from forumapp.models import Thread, ForumSection, Forum, ThreadResponse

admin.site.register(ForumSection)
admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(ThreadResponse)
