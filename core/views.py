from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return render(requests,'index.html')

def signup(requests):
    return render(requests,'signup.html')