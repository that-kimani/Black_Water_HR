import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect

from rest_framework.permissions import AllowAny

class RoleBasedRedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self , request , *args , **kwargs):
        
        # This line will retrieve the authorization header from the request.
        auth_header = request.headers.get('Authorization')

        # If the auth_header variable has nothing, or whatever is in it does not begin with
        # 'Bearer' , give an error response.
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response( {'error': 'Authorization header missing or invalid.'} , status=status.HTTP_401_UNAUTHORIZED )
        
        # Retrieve the token from the authorization header value.
        # (Looks something like this ---> Bearer the-token-here )
        token = auth_header.split(" ")[1]

        try:
            # Decode the payload to get it's data.
            payload = jwt.decode(token , settings.SECRET_KEY , algorithms='HS256')

            # Retrieve the staff category 
            # which will determine a user's destination app.
            staff_category = payload.get('staff_category')

            # Redirect users depending on their staff category
            if staff_category == 'hr':
                return HttpResponseRedirect('/hr-dashboard')
            
            elif staff_category == 'staff':
                return HttpResponseRedirect('/staff-dashboard')
        
        # Handle any token-related issues.(Expiration and Bad tokens.)
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token expired"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except jwt.DecodeError:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)