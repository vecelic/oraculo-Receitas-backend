from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()    
    instructions = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Recipes'
        verbose_name = 'Recipe'
        indexes = [
            models.Index(fields=['title']),
        ]
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Ingredients'
        verbose_name = 'Ingredient'
        indexes = [
            models.Index(fields=['name']),
        ]
class Step(models.Model):
    description = models.TextField()
    order = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    def __str__(self):
        return f"Step {self.order}: {self.description}"
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Steps'
        verbose_name = 'Step'
        indexes = [
            models.Index(fields=['order']),
        ]