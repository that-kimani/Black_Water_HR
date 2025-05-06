import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

from rest_framework.permissions import AllowAny

class RoleBasedRedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self , request , *args , **kwargs):
        

        
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return Response( {'error': 'Authorization header missing or invalid.'} , status=status.HTTP_401_UNAUTHORIZED )
        
        token = auth_header.split("Bearer ")[1].strip().replace('"', '').replace('<', '').replace('>', '')

        # try:
        #     payload = jwt.decode(token , settings.SECRET_KEY , algorithms='HS256')

        #     return (payload)
        
        # except Exception as err:
        #    return Response(f'error:Something went wrong. {err}')

        payload = jwt.decode(token , settings.SECRET_KEY , algorithms='HS256')

        return Response(payload)