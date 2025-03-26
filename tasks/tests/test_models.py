from datetime import datetime

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.utils import timezone

from tasks.models import Position, TaskType, Task


class ModelsTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="QA Engineer")
        self.client = Client()
        self.worker = get_user_model().objects.create_user(
            username="test.user",
            password="test12345",
            position=self.position
        )
        self.client.force_login(self.worker)

        self.task_type = TaskType.objects.create(name="Feature")
        self.task = Task.objects.create(
            name="Test search feature",
            description="A task to test search",
            deadline=timezone.make_aware(
                datetime(2030, 1, 1, 12, 0, 0)
            ), is_completed=False,
            priority="urgent",
            task_type=self.task_type
        )

    def test_task_str(self):
        self.assertEqual(
            str(self.task),
            self.task.name
        )

    def test_worker_str(self):
        self.assertEqual(
            str(self.worker),
            f"{self.worker.first_name} {self.worker.last_name}"
        )

    def test_position_str(self):
        self.assertEqual(str(self.position), self.position.name)

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), self.task_type.name)
