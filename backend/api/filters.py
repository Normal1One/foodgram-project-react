from django_filters import BooleanFilter
from django_filters.widgets import BooleanWidget
from django_filters.rest_framework import (FilterSet,
                                           CharFilter,
                                           AllValuesMultipleFilter)

from .models import Recipe


class IngredientsFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='istartswith')


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
