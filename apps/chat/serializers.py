from rest_framework import serializers

from . import models


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('id', 'email', 'join_date', 'country', 'city', 'display_name', 'avatar')


class MemberSerializer(serializers.ModelSerializer):
    user = AuthUserSerializer()

    class Meta:
        model = models.Member
        fields = ('id', 'user', 'guild', 'admin', 'active', 'banned')


class GuildSerializer(serializers.ModelSerializer):
    creator = AuthUserSerializer()

    class Meta:
        model = models.Guild
        fields = ('id', 'name', 'creator', 'created', 'poster')
