from django.db import models
from authentication.models import CustomUser


class Operation(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_converter")
    format_from = models.TextField(blank=True)
    format_to = models.TextField(blank=True)
    file_url = models.TextField(blank=True)
    operation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.user} {self.format_from} {self.format_to}"
