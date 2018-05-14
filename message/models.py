from django.db import models

# Create your models here.


class Message(models.Model):

    message = models.TextField(null=False)

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)