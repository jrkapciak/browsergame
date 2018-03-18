from ..models import Character

# TODO: TYPINGS


class HealthManager:
    """ Class responsible for character health managing"""

    def __init__(self, character: Character):
        self.character = character
        self.actual_health = self.character.health

    def on_drink_health_potion(self, health_potion):
        self.actual_health += health_potion.value
        self.save_character()

    def on_regeneration(self, value):
        self.actual_health += value
        self.save_character()

    def can_fight(self):
        # TODO: should move constants values to something like configs
        return True if self.actual_health > 50 else False

    def is_dead(self):
        return True if self.actual_health < 1 else False

    def save_character(self):
        self.character.health = self.actual_health
        self.character.save()


class Regeneration:
    """ Class responsible for regeneration"""
    pass
