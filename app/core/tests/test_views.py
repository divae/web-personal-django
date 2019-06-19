from django.test import TestCase

ROOT_TEMPLATE_PATH = 'core/pages/'


class TestMainNavigation(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, ROOT_TEMPLATE_PATH + 'home.html')

    def test_about_me(self):
        response = self.client.get('/about-me/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, ROOT_TEMPLATE_PATH + 'about_me.html')

    def test_portfolio(self):
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, ROOT_TEMPLATE_PATH + 'portfolio.html')

    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, ROOT_TEMPLATE_PATH + 'contact.html')
