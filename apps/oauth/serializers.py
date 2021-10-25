from rest_framework import serializers

from . import models


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('avatar', 'country', 'city', 'display_name')


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialLink
        fields = ('id', 'link')


class UserSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = models.AuthUser
        fields = ('id', 'avatar', 'country', 'city', 'display_name', 'social_links')


class GoogleAuth(serializers.Serializer):
    """ Сериализация данных от Google """

    email = serializers.EmailField()
    token = serializers.CharField()
