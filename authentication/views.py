from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import DetailView, UpdateView
from authentication.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm
from authentication.models import CustomUser, UserType
from authentication.utils import Utils
from subscriptions.models import Subscription


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
            sub = Subscription(user=new_user)
            sub.save()
            Utils.send_verification_email(get_current_site(request), new_user)
            return render(request, 'authentication/signup_done.html')
        return render(request, 'authentication/signup.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'authentication/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "User was logged out")
    return redirect('home')


def email_verify(request, uidb64):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None:
        user.is_verified = True
        user.user_type = UserType.BASIC
        user.save()
    return render(request, 'authentication/verification_done.html', {"username": user.username})


class UserDetails(UpdateView):
    model = CustomUser
    template_name = "authentication/user_details.html"
    form_class = UserUpdateForm
    success_message = "User was updated successfully"
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "User was updated successfully")
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        subscription = Subscription.objects.get(user=user)
        kwargs['instance'] = user
        if user.user_type == "Premium":
            kwargs['initial'] = {'sub_expire_date': subscription.sub_expire_date}
            return kwargs
        else:
            kwargs['initial'] = {'sub_expire_date': subscription.num_of_operations}
            return kwargs
