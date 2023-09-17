from datetime import date
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from ..models import ToDo

class ToDoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username='admin',
            password='testpassword',
            email='admin@example.com'
        )
        self.client.login(username='admin', password='testpassword')

    def test_create_todo(self):
        url = reverse('todo-list-create')
        data = {'title': 'Test Todo', 'date': '2023-09-18'} 

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        todo = ToDo.objects.get(id=response.data['id'])
        self.assertEqual(todo.title, 'Test Todo')

    def test_invalid_todo_creation(self):
        url = reverse('todo-list-create')
        invalid_data = {'title': 'Test Todo', 'date': ''}  # Missing date value

        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_todo_list(self):
        sample_todo = ToDo.objects.create(title='Sample Todo', date=date(2023, 9, 18))

        url = reverse('todo-list-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the response contains the sample todo item
        self.assertTrue(any(todo['id'] == sample_todo.id for todo in response.data))

    def test_retrieve_todo_detail(self):
        todo = ToDo.objects.create(title='Sample Todo', date=date(2023, 9, 18))
        url = reverse('todo-detail', args=[todo.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Sample Todo')
        self.assertEqual(response.data['date'], '2023-09-18')

    def test_update_todo_is_complete(self):
        todo = ToDo.objects.create(title='Test Todo', date=date(2023, 9, 18))
        url = reverse('todo-complete', args=[todo.id])
        updated_data = {'is_complete': True}

        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_complete'])

    def test_update_todo(self):
        todo = ToDo.objects.create(title='Test Todo', date=date(2023, 9, 18))
        url = f"/todos/{todo.id}/"
        updated_data = {'title': 'Updated Todo'}

        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Todo')

