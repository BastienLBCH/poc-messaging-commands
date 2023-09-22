from django.urls import path

from . import views

app_name = "instantMessages"

urlpatterns = [
    path("test", views.test, name="test"),
    path("", views.userCreatedConversation, name="createconversations"),
    path("<str:conversation_id>", views.userSentMessageToConversation, name="sendmessage"),
    path("<str:conversation_id>/delete", views.userDeletedConversation, name="deleteconversation"),
    path("<str:conversation_id>/participants", views.userAddedParticipantToConversation, name="addparticipant"),
    path("<str:conversation_id>/participants/<str:participant_id>", views.userRemovedParticipantToConversation, name="removeparticipant"),
]
