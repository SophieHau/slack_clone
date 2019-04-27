from django.db import models
from user_profile.models import Profile
from django.contrib.auth.models import User


class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='channels')
    users = models.ManyToManyField(User)