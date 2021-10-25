from django.core.validators import FileExtensionValidator
from django.db import models

from ..base.services import get_path_upload_avatar, validate_size_image


class AuthUser(models.Model):
    """ Модель пользователя """

    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    @property
    def is_anonymous(self):
        """ Всегда возвращает False. Способ узнать был ли пользователь анонимен. """

        return False

    @property
    def is_authenticated(self):
        """ Всегда возвращает True. Способ узнать был ли пользователь аутентифицирован. """

        return True

    def __str__(self):
        return self.email


class SocialLink(models.Model):
    """ Модель ссылок на социальные сети. """

    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)

    def __str__(self):
        return str(self.user)
