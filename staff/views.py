from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def StaffDashboard(request):
    return HttpResponse('Staff Dashboard')