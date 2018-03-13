from ..models import Character


class LevelManager:
    """ Class handling character level state (level up, information about need exp)"""

    def __init__(self, character: Character):
        self.character = character

    def next_level_value(self) -> int:
        """ Return needed next level points"""
        return self.character.level * 20  # test value -> we can change it

    def can_level_up(self) -> bool:
        current_exp = self.character.experience_points
        needed_points = self.next_level_value()

        return True if current_exp - needed_points > 0 else False

    def level_up(self):
        if self.can_level_up():
            self.character.level += 1
            self.character.save()

            return True

        return False



