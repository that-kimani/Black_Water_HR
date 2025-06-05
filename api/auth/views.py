from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainpair_Serializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainpair_Serializer