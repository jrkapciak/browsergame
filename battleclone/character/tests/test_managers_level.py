from django.test import TestCase
from mixer.backend.django import mixer
from ..managers.level import LevelManager
from ..models import Character


class LevelManagerTestCase(TestCase):
    def setUp(self):
        self.character = mixer.blend(Character)
        self.level_manager = LevelManager(self.character)

    def tearDown(self):
        Character.objects.get(pk=self.character.pk).delete()
        del self.level_manager

    def test_next_level_value(self):
        self.character.level = 2
        self.assertEqual(self.level_manager.next_level_value(), 40)

        self.character.level = 4
        self.assertEqual(self.level_manager.next_level_value(), 80)

        self.character.level = 10
        self.assertEqual(self.level_manager.next_level_value(), 200)

    def test_can_level_up(self):
        self.character.level = 2
        self.character.experience_points = 200
        self.assertEqual(self.level_manager.can_level_up(), True)

        self.character.level = 5
        self.character.experience_points = 20
        self.assertEqual(self.level_manager.can_level_up(), False)

    def test_level_up(self):
        self.character.level = 2
        self.character.experience_points = 150
        self.character.save()
        self.assertEqual(self.level_manager.level_up(), True)
        self.assertEqual(self.character.level, 3)

        self.character.level = 5
        self.character.experience_points = 2
        self.character.save()
        self.assertEqual(self.level_manager.level_up(), False)
        self.assertEqual(self.character.level, 5)
