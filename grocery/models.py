# grocery/models.py
from django.db import models
from datetime import datetime, timedelta

class GroceryItem(models.Model):
    item = models.CharField(max_length=255)
    expiry_date = models.DateField()

    def __str__(self):
        return self.item
