from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
from api.serializers.auth_serializers import Login_serializer
import jwt
import datetime

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self , request):

        # Use the serializer to check and parse the response for what we need.
        serializer = Login_serializer(data = request.data)

        # If the serializer is valid , generate the validated_data dict
        # and extract the data.
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate the user
            user = authenticate(username=username , password=password)

            # Create a payload to be encoded in the JWT token.
            if user is not None:
                payload = {
                    'id'       : user.id,
                    'username' : user.username,
                    'exp'      : datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                    'iat'      : datetime.datetime.utcnow()

                }

                # Construct the JWT token with the payload.
                token = jwt.encode(payload , settings.SECRET_KEY , algorithm='HS256')

                return Response({'token': token}, status=status.HTTP_200_OK)
            
            else:
                return Response({'error' : 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
def test_view(request):
    return (HttpResponse('Hello World'))
