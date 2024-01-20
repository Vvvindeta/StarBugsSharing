from django.shortcuts import render

# from users.forms import UserLoginForm, UserRegistrationForm

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'form': form})


def login(request):
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

def account(request):
    return render(request, 'users/account.html')