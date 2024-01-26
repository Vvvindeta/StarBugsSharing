from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm

from users.models import User


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:account'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:account'))
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'users/login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


@login_required
def account(request):
    return render(request, 'users/account.html')


def throw(request):
    pass
