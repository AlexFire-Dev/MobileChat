from rest_framework import viewsets, parsers, permissions

from .. import serializers, models
from ...base.permissions import IsAuthor


class MeView(viewsets.ModelViewSet):
    """ Просмотр и редактирование данных пользователя """

    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.MeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()


class UserView(viewsets.ReadOnlyModelViewSet):
    """ Список пользователей """

    queryset = models.AuthUser.objects.all().prefetch_related('social_links')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SocialLinkView(viewsets.ModelViewSet):
    """ CRUD ссылок соц. сетей пользователя """

    serializer_class = serializers.SocialLinkSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return None
        return self.request.user.social_links.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
