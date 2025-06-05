from django.urls import path
from . import views

urlpatterns = [
    path('staff-dashboard' , views.StaffDashboardView.as_view() , name='Staff-dashboard' )
]