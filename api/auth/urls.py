from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('' , MyTokenObtainPairView.as_view() , name= 'token-obtain_pair'),
    path('' , TokenRefreshView.as_view() , name='token_refresh'),
]