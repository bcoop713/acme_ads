from django.test import TestCase


class HomePageTest(TestCase):

	def test_homepage_uses_proper_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'index.html')