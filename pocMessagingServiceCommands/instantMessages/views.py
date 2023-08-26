from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers.serializers import \
    UserCreatedConversationModelSerializer, \
    UserAddedParticipantToConversationModelSerializer, \
    UserRemovedParticipantToConversationModelSerializer, \
    UserSentMessageToConversationModelSerializer, \
    UserDeletedConversationModelSerializer

import jwt


def index(request):
    return HttpResponse("Hello, world. You're at the messages index.")


@api_view(["POST"])
def userCreatedConversation(request):
    """
    Register an event signaling the user created a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")

    # data = JSONParser().parse(request)
    data = request.data.copy()
    data["creator_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]

    serializer = UserCreatedConversationModelSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def userAddedParticipantToConversation(request):
    """
    Register an event that a user added a participant to a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")
    data = request.data.copy()
    data["user_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]

    serializer = UserAddedParticipantToConversationModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def userRemovedParticipantToConversation(request):
    """
    Register an event that a user removed a participant to a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")
    data = request.data.copy()
    data["user_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]

    serializer = UserRemovedParticipantToConversationModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def userSentMessageToConversation(request):
    """
    Register an event that a user sent a message to a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")
    data = request.data.copy()
    data["user_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]

    serializer = UserSentMessageToConversationModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userDeletedConversation(request):
    """
    Register an event that a user added a participant to a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")
    data = request.data.copy()
    data["user_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]

    serializer = UserDeletedConversationModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



