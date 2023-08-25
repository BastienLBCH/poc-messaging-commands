from django.conf import settings
import requests
import json
import jwt


keycloak_public_key = settings.KEYCLOAK_PUBLIC_KEY
keycloak_alg=settings.KEYCLOAK_ALG


class JWTAuthentificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """
        Middleware verifying each request is identified
        :param request:
        :return:
        """

        bearer = request.headers["Authorization"].split(" ")[1]

        payload = None
        key = '-----BEGIN PUBLIC KEY-----\n' + keycloak_public_key + '\n-----END PUBLIC KEY-----'
        try:
            payload = jwt.decode(
                bearer,
                key,
                algorithms=keycloak_alg,
                audience="account"
            )
        except Exception:
            raise Exception("User is not correctly logged in")

        print(payload)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response