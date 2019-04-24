from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile = Profile.objects.get(user_id=user.id)
            return redirect('user_profile:profile', profile_id=profile.id)
        # else:
        #     return redirect('user_profile:signup')

    return render(request, 'login.html')


def show_profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    return render(request, 'profile.html', {
            'profile': profile
        })