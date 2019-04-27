from django.db import models
from user_profile.models import Profile
from chats.models import Channel


class Message(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="messages")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="messages")
