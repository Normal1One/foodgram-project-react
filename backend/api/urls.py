from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ShoppingCartView,
                    TagViewSet,
                    IngredientViewSet,
                    RecipeViewSet)

router = DefaultRouter()
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls)),
    path('recipes/<int:pk>/shopping_cart/',
         ShoppingCartView.as_view(), name='shopping_cart')
]
