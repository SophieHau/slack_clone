from django.shortcuts import render, redirect
from .models import Channel
from message.models import Message
from django.db.models import Q


def show_channels(request):
	channels = Channel.objects.all()
	return render(request, 'channels_list.html', {
		'channels': channels
		})

def search_channel(request):
	context = None
	if request.method != 'POST':
		return redirect('chats:channels')

	text = request.POST.get('search', '')
	results = Channel.objects.filter(
		Q(name__icontains=text) |
		Q(description__icontains=text)
		)

	return render(request, 'channels_list.html', {
            'channels': results,
        })

def show_channel(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    messages = Message.objects.filter(channel_id=channel.id)
    return render(request, 'channel.html', {
            'channel': channel,
            'messages': messages
        })