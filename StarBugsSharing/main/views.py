from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'main/index.html')


def faq(request):
    return render(request, 'main/faq.html')


def premium(request):
    return render(request, 'main/premium.html')


def rules(request):
    return render(request, 'main/rules.html')
