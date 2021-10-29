from django.core.validators import FileExtensionValidator
from django.db import models

from ..base.services import get_path_upload_poster, validate_size_image
from apps.oauth.models import AuthUser


class Guild(models.Model):
    name = models.CharField(max_length=30)
    creator = models.ForeignKey(AuthUser, on_delete=models.PROTECT, related_name='guilds')
    created = models.DateField(auto_now_add=True)
    poster = models.ImageField(
        upload_to=get_path_upload_poster,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    def __str__(self):
        return self.name


class Member(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.PROTECT, related_name='memberships')
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name='members')
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.guild} - @{self.user}'


class Channel(models.Model):
    name = models.CharField(max_length=30)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name='channels')
    private = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.guild} - #{self.name}'


class Message(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='users_messages')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channels_messages')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.text}'


class Invitation(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name='invitation_links')
    key = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.guild} - {self.key}'
