from rest_framework import serializers
from ..models import UserCreatedConversation, UserAddedParticipantToConversation


# Serializer for the even generated when a user creates a conversation
class UserCreatedConversationModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    creator_id = serializers.CharField(required=True)

    class Meta:
        model = UserCreatedConversation
        fields = "__all__"


# Serializer for the event generated when a user added a participant to a conversation
class UserAddedParticipantToConversationModelSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    participant_id = serializers.CharField(required=True)
    conversation_id = serializers.CharField(required=True)

    class Meta:
        model = UserAddedParticipantToConversation
        fields = "__all__"










