from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def StaffDashboard(request):

    template = loader.get_template('staffDashboard.html')

    return HttpResponse(template.render(request=request))