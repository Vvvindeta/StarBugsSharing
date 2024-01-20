from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


def error_404(request, exception):
    return render(request, '404.html')


# def error_500(request, exception):
#     return render(request, '500.html', status=500)


def index(request):
    return render(request, 'main/index.html')


def faq(request):
    return render(request, 'main/faq.html')


def premium(request):
    return render(request, 'main/premium.html')


def rules(request):
    return render(request, 'main/rules.html')

def rent(request):
    return render(request, 'main/rent.html')