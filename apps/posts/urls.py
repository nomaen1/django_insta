from django.urls import path
from .views import index, explore, messages, posts

urlpatterns = [
    path("", index, name="index"),
    path("explore/", explore, name="explore"),
    path("messages/", messages, name="messages"),
    path("create_posts/", posts, name="posts"),
]