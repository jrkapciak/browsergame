from django.test import TestCase
from mixer.backend.django import mixer
from ..models import Character


class LevelManagerTestCase(TestCase):
    def setUp(self):
        self.character = mixer.blend(Character)

    def tearDown(self):
        Character.objects.get(pk=self.character.pk).delete()

    def test_change_status(self):
        self.assertEqual(self.character.update_status('WORK'), 'WORK')
