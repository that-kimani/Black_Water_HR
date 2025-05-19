from rest_framework.views import APIView
from rest_framework.response import Response

from django.template import loader
from django.http import HttpResponse

from rest_framework.permissions import AllowAny

class serve_homepage(APIView):
    permission_classes = [AllowAny]

    def get(self , request):
        template = loader.get_template('homepage.html')

        return HttpResponse(template.render(request=request))