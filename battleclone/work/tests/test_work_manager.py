from django.test import TestCase
from mixer.backend.django import mixer
from ..managers.work_manager import WorkManager
from ..models import Work
from datetime import datetime, timedelta


class WorkManagerTestCase(TestCase):
    def setUp(self):
        self.work = mixer.blend(Work)
        self.work_manager = WorkManager(self.work)

    def tearDown(self):
        Work.objects.get(pk=self.work.pk).delete()
        del self.work_manager

    def test_can_work(self):
        # test default
        self.assertEqual(self.work_manager.can_work(), True)

        # change types a little bit
        self.work.character.status = 'BUSY'
        self.assertEqual(self.work_manager.can_work(), False)

    def test_is_finished(self):
        now = datetime.now()

        day_previous = now - timedelta(hours=24)
        self.work.started = day_previous
        self.work.work_type = 10
        self.assertEqual(self.work_manager.is_finished(), True)

        two_day_previous = now - timedelta(hours=48)
        self.work.started = two_day_previous
        self.work.work_type = 12
        self.assertEqual(self.work_manager.is_finished(), True)

        five_minutes_ago = now - timedelta(minutes=5)
        self.work.started = five_minutes_ago
        self.work.work_type = 5
        self.assertEqual(self.work_manager.is_finished(), False)

    def test_get_reward(self):
        now = datetime.now()
        self.work.started = now - timedelta(hours=24)

        self.work.character.level = 1
        hours = 10
        self.work.work_type = hours
        reward = self.work_manager.get_reward()
        self.assertEqual(reward.money, 200)
        self.assertEqual(reward.exp, 50)

        self.work.character.level = 7
        hours = 7
        self.work.work_type = hours
        reward = self.work_manager.get_reward()
        self.assertEqual(reward.money, 7 * 20 * hours)
