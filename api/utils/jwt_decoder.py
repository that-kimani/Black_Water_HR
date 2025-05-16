from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

import jwt


def decode_jwt_token(token):
        try:
            # Decode the payload to get it's data.
            payload = jwt.decode(token , settings.SECRET_KEY , algorithms='HS256')

            # Retrieve the staff category 
            # which will determine a user's destination app.
            return payload
        
        # Handle any token-related issues.(Expiration and Bad tokens.)
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token expired"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except jwt.DecodeError:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)