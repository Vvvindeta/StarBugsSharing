from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Если вы хотите выполнить вход пользователя после успешной регистрации, раскомментируйте следующую строку
            # login(request, user)
            return redirect('login')  # Замените 'login' на ваш путь для входа
    else:
        form = UserCreationForm()
    return render(request, 'main/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Замените 'home' на ваш путь для домашней страницы
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def index(request):
    return render(request, 'main/index.html')


def faq(request):
    return render(request, 'main/faq.html')


def premium(request):
    return render(request, 'main/premium.html')


def rent(request):
    return render(request, 'main/rent.html')


def rules(request):
    return render(request, 'main/rules.html')



def account(request):
    return render(request, 'main/account.html')
