from django.db import models
from django.contrib.auth.models import User

class SavedRecipe(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    ingredients = models.TextField()
    calories = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    carbs = models.CharField(max_length=20)
    fat = models.CharField(max_length=20)
    instructions = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_recipes')

    def __str__(self):
        return self.name




