from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Follow
from api.serializers import FollowSerializer
from api.pagination import FoodgramPagination

User = get_user_model()


class MyUserViewSet(UserViewSet):
    pagination_class = FoodgramPagination

    @action(methods=['POST', 'DELETE'],
            detail=True, permission_classes=[permissions.IsAuthenticated],
            url_path='subscribe', url_name='subscribe')
    def subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        if user == author:
            return Response({'error': 'Нельзя подписаться на сомого себя'})
        if request.method == 'POST':
            follow = Follow.objects.create(user=user, author=author)
            serializer = FollowSerializer(
                follow, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        follow = Follow.objects.filter(user=user, author=author)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=False,
            permission_classes=[permissions.IsAuthenticated],
            url_path='subscriptions', url_name='subscriptions')
    def subscriptions(self, request):
        queryset = Follow.objects.filter(user=request.user)
        serializer = FollowSerializer(
            self.paginate_queryset(queryset),
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)
