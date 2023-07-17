from django.contrib import admin
from apps.posts.models import StatusModel, Posts

admin.site.register(StatusModel)
admin.site.register(Posts)