# In canteen/models.py

from django.db import models
from django.contrib.auth.models import User

# A profile linked to Django's built-in User model
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college_id = models.CharField(max_length=20, unique=True)
    rfid_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    no_show_strikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

# Model for food categories
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# Model for the individual food items on the menu
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')
    category = models.ForeignKey(Category, related_name='food_items', on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    stock_count = models.PositiveIntegerField(default=100) # Default stock

    def __str__(self):
        return self.name

# The main Order model
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING_PAYMENT', 'Pending Payment'),
        ('PAID', 'Paid'),
        ('IN_PROGRESS', 'In Progress'),
        ('READY_FOR_PICKUP', 'Ready for Pickup'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('REFUNDED', 'Refunded'),
    ]
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING_PAYMENT')
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_slot = models.CharField(max_length=50) # e.g., "11:00 AM - 11:15 AM"
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.student.user.username}"

# The items within an order (linking Orders and FoodItems)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.food_item.name}"