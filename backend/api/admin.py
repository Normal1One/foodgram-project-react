from django.contrib import admin

from .models import Favorite, Recipe, Ingredient, ShoppingCart, Tag, IngredientAmount


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'name',
        'count'
    ]
    list_editable = ['author', 'name']
    list_filter = ['author', 'tags']

    def count(self, obj):
        return obj.favorites.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'measurement_unit',
    ]
    list_editable = ['name', 'measurement_unit']
    list_filter = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'color',
        'slug',
    ]
    list_editable = ['name', 'color', 'slug']


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'ingredient',
        'amount',
    ]
    list_editable = ['ingredient', 'amount']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'recipe',
        'user'
    ]

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'recipe',
        'user'
    ]
