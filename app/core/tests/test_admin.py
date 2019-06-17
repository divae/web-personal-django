from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='yo@gmia.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='tes@gmail.com',
            password='pass123',
            name='Test unser full name'
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        result = self.client.get(url)

        self.assertContains(result, self.user.name)
        self.assertContains(result, self.user.email)

    def test_user_change_page(self):
        http_connect_ok = 200
        url = reverse('admin:core_user_change', args=[self.user.id])
        result = self.client.get(url)

        self.assertEqual(result.status_code, http_connect_ok)

    def test_create_user_page(self):
        http_connect_ok = 200
        url = reverse('admin:core_user_add')
        result = self.client.get(url)

        self.assertEqual(result.status_code, http_connect_ok)
