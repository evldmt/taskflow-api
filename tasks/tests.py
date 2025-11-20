import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestTasks:

    def setup_method(self):

        self.user = User.objects.create_user(email='vadimdev', password='9987')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.url = '/api/tasks/'

    def test_create_task(self):
        data = {'title': 'Auto Test Task'}
        response = self.client.post(self.url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'Auto Test Task'

        assert response.data['id'] > 0

    def test_get_my_tasks(self):

        from .models import Task
        Task.objects.create(owner=self.user, title="DB Task")

        response = self.client.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['title'] == "DB Task"