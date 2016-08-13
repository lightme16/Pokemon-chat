from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Chat(models.Model):
    date = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

