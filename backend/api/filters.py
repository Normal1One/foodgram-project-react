from django_filters import (
    BooleanFilter, FilterSet, CharFilter, AllValuesMultipleFilter)
from django_filters.widgets import BooleanWidget

from .models import Ingredient, Recipe


class IngredientsFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name', 'measurement_unit')


class RecipesFilter(FilterSet):
    tags = AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = BooleanFilter(
        method='get_favorite',
        widget=BooleanWidget()
    )
    is_in_shopping_cart = BooleanFilter(
        method='get_is_in_shopping_cart',
        widget=BooleanWidget()
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')

    def get_favorite(self, queryset, name, value):
        user = self.request.user
        if value:
            return Recipe.objects.filter(favorites__user=user)
        return Recipe.objects.all()

    def get_is_in_shopping_cart(self, queryset, name, value):
        user = self.request.user
        if value:
            return Recipe.objects.filter(shoppingcart__user=user)
        return Recipe.objects.all()
