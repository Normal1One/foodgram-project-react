from django_filters.rest_framework import (FilterSet,
                                           CharFilter,
                                           AllValuesMultipleFilter)


class IngredientsFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='istartswith')


class TagsFilter(FilterSet):
    tags = AllValuesMultipleFilter(field_name='tags__slug')
