from django.contrib import admin

from .models import Recipe, Ingredient, Tag, IngredientAmount


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'name',
    ]
    list_editable = ['author', 'name']
    list_filter = ['author', 'tags']


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
