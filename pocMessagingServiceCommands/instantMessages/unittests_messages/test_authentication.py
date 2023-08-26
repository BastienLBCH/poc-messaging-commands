from django.test import TestCase, Client
from rest_framework import status
from django.conf import settings
import json
import requests

client = Client()


def get_jwt_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = f"client_id={settings.CLIENT_ID}&username={settings.USERNAME_TEST}&password={settings.PASSWORD_TEST}&grant_type=password"

    r = requests.post(headers=headers, data=data, url=settings.KEYCLOAK_TOKEN_URL)
    return r.json()["access_token"]


class AuthentificationTestCase(TestCase):
    def test_user_send_unauthenticated_request(self):
        response = client.get("/messages/")
        self.assertIs(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_send_authenticated_request(self):
        token = get_jwt_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = client.get("/messages/", headers=headers)
        self.assertIs(response.status_code, status.HTTP_200_OK)


