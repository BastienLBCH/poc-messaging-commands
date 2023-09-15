from django.urls import path

from . import views

app_name = "instantMessages"
urlpatterns = [
    path("test/", views.index, name="test"),
    path("createconversation/", views.userCreatedConversation, name="createconversations"),
    path("deleteconversation/", views.userDeletedConversation, name="deleteconversation"),
    path("addparticipant/", views.userAddedParticipantToConversation, name="addparticipant"),
    path("removeparticipants/", views.userRemovedParticipantToConversation, name="removeparticipant"),
    path("sendmessages/", views.userSentMessageToConversation, name="sendmessage"),
]