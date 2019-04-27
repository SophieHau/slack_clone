from django.shortcuts import render, redirect
from .models import Channel
from message.models import Message
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user_profile.models import Profile


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
    user = request.user
    channel.users.add(user)
    channel.save()

    return render(request, 'channel.html', {
        'channel': channel,
        'messages': messages,
        })

def add_channel(request):
    if request.method == "POST":
        name = request.POST['channel_name']
        description = request.POST['channel_description']
        creator_id = request.user.id
        channel = Channel(name=name, description=description, creator_id=creator_id)
        channel.save()
        return redirect('chats:channels')

def open_chat(request, friend_id):
    friend = User.objects.get(id=friend_id)
    user = request.user
    channel = Channel(name="{} & {}".format(user.username, friend.username), description=None, creator_id=user.id)
    channel.save(False)
    channel.users.add(friend)
    channel.save(False)
    channel.users.add(user)
    channel.save()
    messages = Message.objects.filter(channel_id=channel.id)
    return render(request, 'channel.html', {
            'channel': channel,
            'messages': messages,
        })
