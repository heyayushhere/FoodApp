# foodwaste/recipes/models.py
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title


# foodwaste/recipes/models.py
from django.db import models

class PerishableItem(models.Model):
    name = models.CharField(max_length=255)
    estimated_expiration_days = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
