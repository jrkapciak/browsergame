from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Parameters(models.Model):
    """ Character parameters:
    strength, agility, luck etc

    """


class Equipment(models.Model):
    """ Character equipment

        helmet, armor, boots, weapon etc
    """
    pass


class Vehicle(models.Model):
    """ Vehicle like horse or something"""
    pass


class Storage(models.Model):
    """ Storage, place where we put not wearing clothes or unused items"""
    pass


class Character(models.Model):
    nickname = models.CharField(
        verbose_name=_('Nickname'),
        help_text=_("Character's nickname"),
        max_length=30,
    )

    level = models.PositiveSmallIntegerField(
        verbose_name=_("Level"),
        help_text=_("Character's actual level"),
        default=1,
        validators=[MinValueValidator(1)]
    )

    experience_points = models.IntegerField(
        verbose_name=_("Experience points"),
        help_text=_('Actual experience points'),
        default=1,
        validators=[MinValueValidator(1)]
    )

    health = models.PositiveSmallIntegerField(
        verbose_name=_("Health"),
        help_text=_("Actuacl character'health value"),
        default=100,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    action_points = models.PositiveSmallIntegerField(
        verbose_name=_('Action points'),
        help_text=_('Avaiable points to be used in mission etc.'),
        default=1000,
        validators=[MaxValueValidator(1000), MinValueValidator(0)]
    )

    ruby_number = models.PositiveSmallIntegerField(
        verbose_name=_('Ruby number'),
        help_text=_('Number of avaiable rubies'),
        default=0,
        validators=[MaxValueValidator(1000), MinValueValidator(0)]
    )

    parameters = models.OneToOneField(
        to=Parameters,
        on_delete=models.CASCADE,
        verbose_name=_('Parameters'),
        help_text=_("Character's parameters"),
    )

    def __str__(self):
        return '{} level: {} HP:{} AP:{}'.format(
            self.nickname, self.level, self.health, self.action_points
        )
