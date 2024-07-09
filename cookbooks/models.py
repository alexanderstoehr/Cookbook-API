from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Cookbook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cookbooks')

    def __str__(self):
        return self.title