from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.jwt_decoder import decode_jwt_token
from rest_framework.permissions import AllowAny

from staff.models import StaffUser


def make_db_query(employee_ID):
    try:
        requested_user = StaffUser.objects.get(employee_id=employee_ID)

        data = {
            "employee_id" :  requested_user.employee_id,
            "first_name"  :  requested_user.first_name,
            "last_name"   :  requested_user.last_name,
            "job_title"   :  requested_user.job_title,
            "department"  :  requested_user.department,
            "monthly_ctc" :  requested_user.monthly_ctc,
            "date_joined" :  requested_user.date_of_joining,
            "email"       :  requested_user.email,
            "contact"     :  requested_user.contact,

        }
        return (data)
    
    except StaffUser.DoesNotExist:
        return ('User not found')

    
class fetch_data(APIView):
    permission_classes = [AllowAny]


    def get(self , reqeust):
        # Need to find a way to receive user info(employee id or user_type so that 
        # we can use it to make a query in the db.)

        auth_header = reqeust.headers.get('Authorization')

        # If the auth_header variable has nothing, or whatever is in it does not begin with
        # 'Bearer' , give an error response.
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response( {'error': 'Authorization header missing or invalid.'} , status=status.HTTP_401_UNAUTHORIZED )
        
        # Retrieve the token from the authorization header value.
        # (Looks something like this ---> Bearer the-token-here )
        token = auth_header.split(" ")[1]

        payload = decode_jwt_token(token)

        # return Response(payload)

        employee_ID = payload["employee_id"]

        query_feedback = make_db_query(employee_ID)

        return Response(query_feedback)
