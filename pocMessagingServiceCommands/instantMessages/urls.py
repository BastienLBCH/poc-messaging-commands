from django.urls import path

from . import views

app_name = "instantMessages"
urlpatterns = [
    path("", views.index, name="index"),
    path("conversations/", views.userCreatedConversation, name="conversations"),
    path("conversations/participants", views.userAddedParticipantToConversation, name="addparticipant"),
    path("conversations/participants", views.userRemovedParticipantToConversation, name="removeparticipant"),
    path("conversations/messages", views.userSentMessageToConversation, name="sendmessage"),
]