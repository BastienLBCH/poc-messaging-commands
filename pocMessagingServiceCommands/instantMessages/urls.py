from django.urls import path

from . import views

app_name = "instantMessages"
urlpatterns = [
    path("", views.index, name="index"),
    path("conversations/", views.conversations, name="conversations")
]