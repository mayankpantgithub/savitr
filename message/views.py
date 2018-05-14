import json
from django.shortcuts import render
from message.models import Message
from django.http import HttpResponse
# Create your views here.

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


@permission_classes((AllowAny, ))
def add_message(request):
    message = json.loads(request.body).get("message")
    Message.objects.create(message=message)
    response = HttpResponse("Saved")
    return response