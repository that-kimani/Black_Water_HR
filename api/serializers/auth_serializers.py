from django.urls import path , include
from django.contrib.auth.models import User
from rest_framework import routers , serializers , viewsets

class Login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField( write_only = True)