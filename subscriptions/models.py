import datetime
from django.db import models

from authentication.models import CustomUser, UserType


# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_sub")
    num_of_operations = models.IntegerField(default=20)
    sub_start_date = models.DateTimeField(auto_now_add=True, blank=True)
    sub_expire_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.id} {self.user.username} {self.num_of_operations}"

    def check_limit(self):
        if self.user.user_type == UserType.BASIC:
            return self.num_of_operations > 0
        return True

    def operation_decrease(self):
        if self.check_limit():
            self.num_of_operations -= 1
            self.save()
            return self.num_of_operations
        raise ValueError("You don`t have more operations please update your plan")

    def sub_update(self, num_of_days):
        self.sub_expire_date += num_of_days
        return self.sub_expire_date


class SubPlan(models.IntegerChoices):
    MINIMUM = 10
    MIDDLE = 30
    MAXIMUM = 90


class Payment(models.Model):
    subscriptions = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=datetime.datetime.now())
    payment_plan = models.IntegerField(choices=SubPlan.choices)

    def __str__(self):
        return f"{self.id}, {self.subscriptions} {self.payment_date} {self.payment_plan}"
