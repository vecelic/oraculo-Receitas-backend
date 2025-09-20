from rest_framework import serializers
from .models import Recipe, Ingredient, Step

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity', 'unit']
        read_only_fields = ['id']

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'recipe', 'description', 'order']
        read_only_fields = ['id']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    steps = StepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'steps']
        read_only_fields = ['id']
