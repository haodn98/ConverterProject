from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from authentication.models import CustomUser


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(
                                   attrs={'class': "form-control form-control-lg", 'placeholder': 'Enter username'}))

    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'class': "form-control form-control-lg", 'placeholder': 'Enter password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = CustomUser.objects.filter(username=username).first()
            if not qs:
                raise forms.ValidationError("User does not exist")
            if not check_password(password, qs.password):
                raise forms.ValidationError("Wrong password")
            if not qs.is_verified:
                raise forms.ValidationError("User is not verified")
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User is not active ")
        return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(
                                   attrs={'class': "form-control", 'placeholder': 'Enter username'}))

    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(
                                 attrs={'class': "form-control", 'placeholder': 'Enter Email'}))

    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'class': "form-control", 'placeholder': 'Enter password '}))

    password2 = forms.CharField(label="Repeat the password",
                                widget=forms.PasswordInput(
                                    attrs={'class': "form-control", 'placeholder': 'Enter password again'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        qs = CustomUser.objects.filter(username=username)
        if qs:
            raise forms.ValidationError("User with such username already exists")
        if len(username) < 8:
            raise forms.ValidationError("Username should be at least 8 chars ")
        if not any(i.isupper() for i in username) and not any(i.islower() for i in username):
            raise forms.ValidationError(
                "Username should contain at least 8 chars, contain at least 1 lower and 1 upper case letter ")
        return username

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        qs = CustomUser.objects.filter(email=email)
        if qs:
            raise forms.ValidationError("User with such email already exists")
        return email

    def clean_password2(self, *args, **kwargs):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords are different")
        return data['password']
