from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status

from .pagination import FoodgramPagination
from .serializers import (FavoriteAndShoppingCartSerializer,
                          RecipeReadSerializer,
                          RecipeWriteSerializer,
                          TagSerializer, IngredientSerializer)
from .permissions import IsAdminAuthorOrReadOnly
from .models import (IngredientAmount, ShoppingCart, Favorite, Recipe,
                     Tag, Ingredient)
from .filters import IngredientsFilter, TagsFilter


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filterset_class = IngredientsFilter


class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminAuthorOrReadOnly]
    queryset = Recipe.objects.all()
    pagination_class = FoodgramPagination
    filter_class = TagsFilter

    @action(methods=['POST', 'DELETE'], detail=True,
            permission_classes=[permissions.IsAuthenticated],
            url_path='favorite', url_name='favorite')
    def favorite(self, request, pk=None):
        if request.method == 'POST':
            recipe = get_object_or_404(Recipe, id=pk)
            Favorite.objects.create(
                user=request.user,
                recipe=recipe
            )
            serializer = FavoriteAndShoppingCartSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        obj = Favorite.objects.filter(user=request.user, recipe__id=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST', 'DELETE'], detail=True,
            permission_classes=[permissions.IsAuthenticated],
            url_path='shopping_cart', url_name='shopping_cart')
    def shopping_cart(self, request, pk=None):
        if request.method == 'POST':
            recipe = get_object_or_404(Recipe, id=pk)
            ShoppingCart.objects.create(
                user=request.user,
                recipe=recipe
            )
            serializer = FavoriteAndShoppingCartSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        obj = ShoppingCart.objects.filter(user=request.user, recipe__id=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=False,
            permission_classes=[permissions.IsAuthenticated],
            url_path='download_shopping_cart',
            url_name='download_shopping_cart')
    def download_shopping_cart(self, request):
        cart = request.user.shoppingcart_set.all()
        buying_list = {}
        for item in cart:
            recipe = item.recipe
            ingredient_amount = IngredientAmount.objects.filter(
                recipe=recipe
            )
            for item in ingredient_amount:
                amount = item.amount
                name = item.ingredient.name
                measurement_unit = item.ingredient.measurement_unit
                if name not in buying_list:
                    buying_list[name] = {
                        'amount': amount,
                        'measurement_unit': measurement_unit
                    }
                else:
                    buying_list[name]['amount'] = (buying_list[name]
                                                   ['amount'] + amount)
        shopping_list = []
        for item in buying_list:
            shopping_list.append(
                f'{item} - {buying_list[item]["amount"]}'
                f'{buying_list[item]["measurement_unit"]}\n'
            )
        response = HttpResponse(shopping_list,
                                content_type='application/pdf')
        response['Content-Disposition'] = ('inline;'
                                           'filename="shopping_list.pdf"')
        return response

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return RecipeReadSerializer
        return RecipeWriteSerializer
