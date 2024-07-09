from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(to=User, related_name='favorites', on_delete=models.CASCADE)
    recipe = models.ForeignKey('recipes.Recipe', related_name='favorites', on_delete=models.CASCADE, null=True, blank=True)
    cookbook = models.ForeignKey('cookbooks.Cookbook', related_name='favorites', on_delete=models.CASCADE, null=True, blank=True)
