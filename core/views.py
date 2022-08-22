from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Profile
def index(requests):
    return render(requests,'index.html')

def signup(requests):
    if requests.method == 'POST':
        username=requests.POST['username']
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
            else :
                user = User.objects.create_user(email=email,username=username,password=password1)
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,profile_id=user_model.id)
                new_profile.save()
                return redirect('signup')

        else:
            messages.info(requests,'The given passwords dont match')
            return redirect('signup')
        return HttpResponse('hello')
    else:
        return render(requests,'signup.html')

def signin(requests):
    if requests.method=="POST":
        username = requests.POST['username']
        password = requests.POST['password']
        user_model = User.objects.get(username=username)
        print('hello')
        if user_model != None:
            if user_model.password == password:
                HttpResponse('Correct User Password')
            else :
                messages.info(requests,'password doesnt match')
                return redirect('signin')
        else :
            messages.info(requests,'username doesnt exists')
            return redirect('signin')
    return render(requests,'signin.html')