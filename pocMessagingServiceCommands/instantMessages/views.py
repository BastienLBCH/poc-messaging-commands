from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers.conversations import UserCreatedConversationSerializerCreate, UserCreatedConversationModelSerializer
import jwt


def index(request):
    return HttpResponse("Hello, world. You're at the messages index.")


@api_view(["POST"])
def conversations(request):
    """
    create a new conversation
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







