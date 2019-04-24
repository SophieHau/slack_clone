from django.shortcuts import render, redirect
from .models import Profile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile = Profile.objects.get(user_id=user.id)
            return redirect('user_profile:show_profile', profile_id=profile.id)
        else:
            return redirect('user_profile:signup')

    return render(request, 'login.html')


@login_required(login_url='/accounts/login/')
def show_profile(request, profile_id):
    user_profile = Profile.objects.get(pk=profile_id)
    if request.method == 'POST' and request.FILES['image']:
        profile_pic = request.FILES['image']
        fs = FileSystemStorage(location='media/images', base_url='/media/images/')
        filename = fs.save(profile_pic.name, profile_pic)
        uploaded_file_url = fs.url(filename)
        user_profile.pic = uploaded_file_url
        user_profile.save()

    return render(request, 'profile.html', {
            'profile': user_profile,
        })

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        bio = request.POST['bio']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, username=username, password=password)
        user.save()
        profile = Profile(user=user, bio=bio)
        profile.save()
        return redirect('user_profile:show_profile', profile_id=profile.id)

    return render(request, 'signup.html')
