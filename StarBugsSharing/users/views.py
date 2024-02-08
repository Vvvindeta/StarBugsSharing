from datetime import datetime, timezone, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth


from users.forms import UserLoginForm, UserRegistrationForm

from users.models import User
from rovers.models import Using, Rover


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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:account'))
    else:
        form = UserRegistrationForm(instance=request.user)
    user_usings = Using.objects.filter(user=request.user)
    context = {
        'usings_with_total': list(zip(user_usings, calculate_rent_cost(user_usings))),
        'usings': user_usings,
        'form': form,
    }
    return render(request, 'users/account.html', context)


@login_required
def increase_balance(request):
    user = request.user
    user.balance_value += 500
    user.save()
    return redirect('users:account')


def calculate_rent_cost(using):
    total = []
    for use in using:
        rate = float(Rover.objects.filter(rover_id=use.rover_id).first().rate)
        rent_time = use.end_time - use.start_time if use.end_time else datetime.now(timezone(timedelta(hours=3))) - use.start_time
        total.append(round(rate * rent_time.total_seconds() / 60, 2))
    return total
