
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate
from django.http import JsonResponse
import requests
from string import Template
from django.contrib import messages
from localStoragePy import localStoragePy
# Create your views here.

from django.shortcuts import render,redirect

def LoginView(request):
    message = ""
    localStorage = localStoragePy('user','text')
    access_token = localStorage.getItem('token')
    #print(access_token)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            payload = {
                'username': username,
                'password':password,
            }
            api_url = 'http://127.0.0.1:3000'
            headers = {
                'Authorization': f'Bearer {access_token}' ,
                'Content-Type': 'application/json'
            }
            response = requests.post(api_url, json=payload,headers=headers)
            data = response.json()
            if response.status_code == 200:
                token = data['tokens']
                localStorage.setItem('token', token)
                messages.success(request, 'You have been successfully logged in.')
            else :
                messages.error(request, 'Incorrect username or password.')
    else:
        form = RegisterForm()
        
    return render(request, "website/login.html",{"form":form,"script":message})

def RegisterView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            payload = {
                'username': username,
                'password':password,
                'email': email,
                'first_name':first_name,
                'last_name':last_name
            }
            api_url = 'http://127.0.0.1:3000/register/'
            response = requests.post(api_url, json=payload)
            if response.status_code == 201:
                messages.success(request, 'Account Registered.')
                return redirect("login")
            else:
                messages.warning(request, 'Username already taken.')
        else:
            messages.error(request, 'Account is not created.')
    else:
        form = RegisterForm()
    return render(request, "website/register.html",{"form":form})

def LoggedInPageView(request):
    return render(request, "website/loggedinpage.html")
