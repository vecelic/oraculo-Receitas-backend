import google.generativeai as genai
from decouple import config
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Recipe, Ingredient, Step
from .serializers import RecipeSerializer, IngredientSerializer, StepSerializer
# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

@api_view(['POST'])
def generate_recipe(request):
    ingredients = request.data.get('ingredients', '')
    try:
        genai.configure(api_key=config('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        prompt = f"Aja como um chef de cozinha experiente. Crie uma receita criativa e fácil de seguir, com título, ingredientes e um passo a passo claro, mas sucinto, usando apenas os seguintes itens: {ingredients}. Não use nenhum outro ingrediente além dos listados."
        response = model.generate_content(prompt)
        recipe_text = response.text
        response_data = {'recipe_text': recipe_text}
        return Response(response_data)
    except Exception as e:
        print(f"Erro ao comunicar com o Oráculo Gemini: {e}")
        return Response(
        {'error': 'O Oráculo não respondeu. Tente novamente mais tarde.'},
        status=503 # Service Unavailable
        )
    