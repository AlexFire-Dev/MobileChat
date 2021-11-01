from django.contrib import admin

from . import models


@admin.register(models.Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    list_display_links = ('name',)


@admin.register(models.Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'guild', 'admin', 'active', 'banned')


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author')


@admin.register(models.Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'guild', 'key')
