# In canteen/admin.py

from django.contrib import admin
from .models import StudentProfile, Category, FoodItem, Order, OrderItem

# Register your models here so they appear in the admin panel
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(Order)
admin.site.register(OrderItem)