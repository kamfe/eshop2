from django.test import TestCase


class HomePageTestCase(TestCase):
    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'products/index.html')
