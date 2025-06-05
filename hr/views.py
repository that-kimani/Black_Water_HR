from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsHRUser

# Create your views here.
class HRDashboardView(APIView):
    permission_classes = [IsHRUser]

    def get(self , request):
        return Response({'message' : 'Welcome to the HR Dashboard.'})