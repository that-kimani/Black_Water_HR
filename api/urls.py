from django.urls import path
from .views import auth_views
from .views import redirect_views

urlpatterns = {
    path('api/login' , auth_views.LoginView.as_view() ,name='login_endpoint'),
    path('api/redirect' , redirect_views.RoleBasedRedirectView.as_view() , name='redirect_endpoint')
}