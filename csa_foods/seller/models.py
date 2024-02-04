from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# class Order(models.Model):
#     food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     ordered_at = models.DateTimeField(auto_now_add=True)
#     is_delivered = models.BooleanField(default=False)


class Restaurant(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(default='default_image.png', upload_to='restaurant_images')
    wallet_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)], default=5.00)
    opening_time = models.TimeField(null=True)
    closing_time = models.TimeField(null=True)
    non_veg_available = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.restaurant_name}"


class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)], default=5.00)
    description = models.TextField()
    image = models.ImageField(upload_to='food_images', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.restaurant} - {self.name}"
