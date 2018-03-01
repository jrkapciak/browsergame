from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_('User'),
        help_text=_("User assigned to this profile."),
    )

    description = models.CharField(
        max_length=255,
        verbose_name=_('Description'),
        help_text=_('Put your profile description'),
        null=True, blank=True
    )

    avatar = models.ImageField(
        verbose_name=_('Image'),
        help_text=_('Your account image'),
        null=True, blank=True
    )

    def __str__(self):
        return self.user.username
