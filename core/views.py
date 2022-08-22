from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile


@login_required(login_url='signin')
def index(requests):
    return render(requests, 'index.html')


def signup(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        email = requests.POST['email-box']
        password1 = requests.POST['password-box']
        password2 = requests.POST['password_box2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(requests, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(requests, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=email, username=username, password=password1)
                user.save()
                user_login = auth.authenticate(username=username, password=password1)
                auth.login(requests, user_login)
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, profile_id=user_model.id)
                new_profile.save()
                return redirect('settings')

        else:
            messages.info(requests, 'The given passwords dont match')
            return redirect('signup')
        return HttpResponse('hello')
    else:
        return render(requests, 'signup.html')


def signin(requests):
    if requests.method == "POST":
        username = requests.POST['username']
        password = requests.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(requests, user)
            return redirect('/')
        else:
            messages.info(requests, 'credentials are invalid')
            return redirect('signin')

        '''user_model = User.objects.get(username=username)
        if user_model is not None:
            if user_model.password == password:
                HttpResponse('Correct User Password')
            else:
                messages.info(requests, 'password doesnt match')
                return redirect('signin')
        else:
            messages.info(requests, 'username doesnt exists')
            return redirect('signin')'''
    else:
        return render(requests, 'signin.html')


@login_required(login_url='signin')
def logout(requests):
    # Add feature: Ask for confirmation for logout
    auth.logout(requests)
    return redirect(signin)


@login_required(login_url='signin')
def settings(requests):
    user_profile =Profile.objects.get(user=requests.user)
    if requests.method == "POST":
        user_profile.bio = requests.POST['bio']
        user_profile.location = requests.POST['location']
        if requests.FILES.get('image') is None:
            user_profile.profile_image = user_profile.profile_image
        else:
            user_profile.profile_image = requests.FILES.get('image')
        user_profile.save()
        return redirect('/')

    return render(requests, 'settings.html',{"user_profile": user_profile})
