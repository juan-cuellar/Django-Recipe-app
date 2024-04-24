from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    ingredients = models.CharField(max_length=200, null=True, blank=True)
    preparation = models.TextField()
    image = models.ImageField(upload_to='recipes_image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name