from django.urls import path
from . import views

urlpatterns = [
    path('hr-dashboard' , views.HrDashboard , name='hr-dashboard' )
]