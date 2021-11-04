from django.db.models import QuerySet
from rest_framework import viewsets, parsers, permissions, status
from rest_framework.response import Response

from . import models, serializers
from ..oauth.models import AuthUser


class GuildView(viewsets.ModelViewSet):
    """ Управление сервером """

    serializer_class = serializers.GuildSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return None
        return models.Guild.objects.filter(members__user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        guild = serializer.save(creator=request.user)
        models.Member.objects.create(guild=guild, user=request.user)
        models.Channel.objects.create(guild=guild, name='Основной')

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
