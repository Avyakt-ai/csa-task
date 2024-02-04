from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    wallet_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"
