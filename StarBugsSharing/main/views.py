from django.shortcuts import render


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


def login(request):
    return render(request, 'main/login.html')


def registration(request):
    return render(request, 'main/registration.html')