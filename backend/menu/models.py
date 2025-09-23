# backend/menu/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')
    category = models.ForeignKey(Category, related_name='food_items', on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    stock_count = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name