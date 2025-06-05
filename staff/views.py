from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsStaffUser

# Create your views here.
class StaffDashboardView(APIView):
    permission_classes = [IsStaffUser]

    def get(self , request):
        return Response({'message' : 'Welcome to the Staff Dashboard.'})