from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

"""
Here I have defined an example class 'Mods'. Once the client is authenticated, it can request objects of 'Mods' class
and display it back on the client side.
"""


class News(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="")
    image = models.FileField()

    def __str__(self):
        return f"{self.name} - {self.content}"
