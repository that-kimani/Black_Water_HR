from django.urls import path
from .views import auth_views , redirect_views , userData_request_views , homepage_views

urlpatterns = {
    path('api/login' , auth_views.LoginView.as_view() ,name='login_endpoint'),
    path('api/redirect' , redirect_views.RoleBasedRedirectView.as_view() , name='redirect_endpoint'),
    path('api/get_user_data' , userData_request_views.fetch_data.as_view() , name='fetch_data_endpoint'),
    path('' , homepage_views.serve_homepage.as_view() , name='serve_homepage_endpoint')
}