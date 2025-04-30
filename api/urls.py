from django.urls import path
from .views import auth_views

urlpatterns = {
    path('api/login' , auth_views.LoginView.as_view() ,name='login_endpoint'),
    path('api/test_url', auth_views.test_view , name= 'test_view'),
}