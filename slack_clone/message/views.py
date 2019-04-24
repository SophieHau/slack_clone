from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from chats.models import Channel
from .models import Message


@login_required
def add_message(request, channel_id):
	channel = Channel.objects.get(pk=channel_id)
	if request.method == 'POST':
		text = request.POST['message_text']
		author = request.user.id
		pub_date = timezone.now()
		m = Message(text=text, author_id=author, pub_date=pub_date, channel_id=channel.id)
		m.save()
		return redirect('chats:channel', channel_id=channel.id)
