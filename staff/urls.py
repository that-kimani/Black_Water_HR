from django.urls import path
from . import views

urlpatterns = [
    path('staff-dashboard' , views.StaffDashboard , name='Staff-dashboard' )
]