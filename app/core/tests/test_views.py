from django.test import TestCase


class TestMainNavigation(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_about_me(self):
        response = self.client.get('/about-me/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about_me.html')

    def test_portfolio(self):
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/portfolio.html')

    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')
