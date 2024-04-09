from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from authentication.forms import UserLoginForm, UserRegistrationForm


# Create your views here.

def home(request):
    return render(request, 'authentication/index.html')


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, f"{username} was logged in")
        return render(request, 'authentication/index.html')
    return render(request, 'authentication/login.html', {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'authentication/signup_done.html')
        return render(request, 'authentication/signup.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'authentication/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "User was logged out")
    return redirect('home')
