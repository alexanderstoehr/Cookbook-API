from django.db import models

from cookbooks.models import Cookbook
from ingredients.models import Ingredient
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Recipe(models.Model):
    EASY = 1
    INTERMEDIATE = 2
    HARD = 3

    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (INTERMEDIATE, 'Intermediate'),
        (HARD, 'Hard'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cookbook = models.ManyToManyField(to=Cookbook, related_name='recipes')
    ingredients = models.ManyToManyField(to=Ingredient, related_name='recipes')

    def __str__(self):
        return f"Recipe {self.id}: {self.title}"