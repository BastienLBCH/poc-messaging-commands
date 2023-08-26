from rest_framework import serializers
from ..models import userCreatedConversation


class UserCreatedConversationSerializerCreate(serializers.Serializer):
    name = serializers.CharField()
    creator_id = serializers.CharField()

    def create(self, validated_data):
        return userCreatedConversation(**validated_data)


class UserCreatedConversationModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    creator_id = serializers.CharField(required=True)

    class Meta:
        model = userCreatedConversation
        fields = "__all__"



