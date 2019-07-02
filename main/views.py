from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import logout as dj_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
from django.http import Http404
from .models import *
from .forms import *


def home(request):
    messages.add_message(request, messages.INFO, 'Sample Message')
    return render(request, 'main/home.html', {'current_user' : request.user})


def login(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER')) # already logged in
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                dj_login(request, user)
            else:
                return redirect('login') # try again
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form, 'current_user' : request.user})


def logout(request):
    if request.user.is_authenticated:
        dj_logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def register(request):
    if request.method == "POST" and not request.user.is_authenticated:
        form = RegisterForm(request.POST)
        if form.is_valid():
            #new_user = form.save(commit=False)
            new_base_user = User(username=form.cleaned_data['username'])
            new_base_user.save()
            new_base_user.set_password(form.cleaned_data['password'])
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            new_base_user.first_name=first_name
            new_base_user.last_name=last_name
            new_base_user.save()

            new_user = UserExtras(user=new_base_user)
            new_user.save()

            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form, 'current_user': request.user})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    user_extra = UserExtras.objects.get(user=request.user)
    return render(request, 'main/profile.html', {'current_user': request.user, 'user_extras': user_extra})