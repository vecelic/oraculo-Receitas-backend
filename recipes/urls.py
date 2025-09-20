from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, IngredientViewSet, StepViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'steps', StepViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate/', views.generate_recipe, name='generate-recipe'),
]