from django.urls import path , include

# urlpatterns = {
#     path('api/login' , auth_views.LoginView.as_view() ,name='login_endpoint'),
#     path('api/redirect' , redirect_views.RoleBasedRedirectView.as_view() , name='redirect_endpoint'),
#     path('api/get_user_data' , userData_request_views.fetch_data.as_view() , name='fetch_data_endpoint'),
#     path('' , homepage_views.serve_homepage.as_view() , name='serve_homepage_endpoint'),
#     path('unauthorized' , homepage_views.serve_unauthorized_page.as_view() , name='serve_unauthorized_endpoint')

# }

urlpatterns = [
    # Authentication routes
    path('auth/', include('api.auth.urls')),

    # HR dashboard and operations
    path('hr/', include('hr.urls')),

    # Staff dashboard and operations
    path('staff/', include('staff.urls')),
]