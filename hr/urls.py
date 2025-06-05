from django.urls import path
from . import views

urlpatterns = [
    path('hr-dashboard' , views.HRDashboardView.as_view() , name='hr-dashboard' )
]