from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
@permission_classes((AllowAny, ))
def home(request):
    response = HttpResponse("Welcome to griha")
    return response
