from django.conf.urls import include, url
from django.contrib import admin
from message import views


urlpatterns = [
    url(r'^add_message/$', views.add_message),

]