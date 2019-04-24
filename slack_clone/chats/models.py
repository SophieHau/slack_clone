from django.db import models
from user_profile.models import Profile


class Channel(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	creator = models.ForeignKey(Profile, on_delete=models.CASCADE)