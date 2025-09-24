# dashboard/models.py
from django.db import models

class DashboardMetric(models.Model):
    name = models.CharField(max_length=100)
    value = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.value}"