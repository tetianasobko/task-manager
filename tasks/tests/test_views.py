from datetime import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from tasks.models import Position, TaskType, Task


class SearchViewsTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.client = Client()
        self.worker = get_user_model().objects.create_user(
            username="test.user",
            password="test12345",
            position=self.position
        )
        self.client.force_login(self.worker)

        self.task_type = TaskType.objects.create(name="Feature")
        self.task1 = Task.objects.create(
            name="Implement search feature",
            description="A task to implement search",
            deadline=timezone.make_aware(
                datetime(2030, 1, 1, 12, 0, 0)
            ), is_completed=False,
            priority="urgent",
            task_type=self.task_type
        )
        self.task2 = Task.objects.create(
            name="Test search functionality",
            description="Write tests for search",
            deadline=timezone.make_aware(
                datetime(2030, 1, 1, 12, 0, 0)
            ), is_completed=False,
            priority="high",
            task_type=self.task_type
        )
        self.task3 = Task.objects.create(
            name="Fix minor bug",
            description="A task without search",
            deadline=timezone.make_aware(
                datetime(2030, 1, 1, 12, 0, 0)
            ),
            is_completed=True,
            priority="low",
            task_type=self.task_type
        )

    def test_task_search(self):
        response = self.client.get(
            reverse("tasks:task-list"),
            {"name": "search"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["task_list"]), 2)

        response = self.client.get(
            reverse("tasks:task-list"),
            {"name": ""}
        )
        self.assertEqual(len(response.context["task_list"]), 3)

    def test_worker_search(self):
        response = self.client.get(
            reverse("tasks:worker-list"),
            {"username": "test.user"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["worker_list"]), 1)

    def test_position_search(self):
        response = self.client.get(
            reverse("tasks:position-list"),
            {"name": "dev"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["position_list"]), 1)

    def test_task_type_search(self):
        response = self.client.get(
            reverse("tasks:task-type-list"),
            {"name": "feature"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["task_type_list"]), 1)

    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get(reverse("tasks:worker-list"))
        self.assertNotEqual(response.status_code, 200)
