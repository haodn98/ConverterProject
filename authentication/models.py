from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user: CustomUser = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.registration_date = datetime.now()
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UserType(models.TextChoices):
    PREMIUM = "Premium"
    BASIC = "Basic"
    UNVERIFIED = "Unverified"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=320)
    first_name = models.TextField(max_length=100, default=" ")
    last_name = models.TextField(max_length=100, default=" ")
    user_type = models.TextField(choices=UserType.choices, blank=True, default=UserType.UNVERIFIED)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ["email", "password"]
    USERNAME_FIELD = "username"
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_email(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"



