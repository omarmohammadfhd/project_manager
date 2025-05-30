from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Project, Task

class ProjectAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='testpass')
        self.client.login(username='user1', password='testpass')

    def test_create_project(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/projects/', {'title': 'New Project', 'description': 'Test Project'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TaskFilterSearchTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user2', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_filter_tasks(self):
        response = self.client.get('/api/tasks/?status=done')
        self.assertEqual(response.status_code, status.HTTP_200_OK)