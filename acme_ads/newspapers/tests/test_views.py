from django.test import TestCase
from newspapers.models import Newspaper


class CreateNewspaperTest(TestCase):

	def test_uses_proper_template(self):
		response = self.client.get('/newspapers/create/')
		self.assertTemplateUsed(response, 'create_newspaper.html')

	def test_save_newspaper_on_post(self):
		response = self.client.post(
			'/newspapers/create/',
			data={'name': 'Test Newspaper 1'}
		)

		self.assertEqual(Newspaper.objects.count(), 1)
		new_newspaper = Newspaper.objects.first()
		self.assertEqual(new_newspaper.name, 'Test Newspaper 1')


class NewspaperDetailTest(TestCase):

	def setUp(self):
		newspaper1 = Newspaper()
		newspaper1.name = 'Test Newspaper 1'
		newspaper1.save()

		newspaper2 = Newspaper()
		newspaper2.name = 'Test Newspaper 2'
		newspaper2.save()

	def test_newspaper_detail_uses_proper_template(self):
		response = self.client.get('/newspapers/1/')
		self.assertTemplateUsed(response, 'newspaper_detail.html')

	def test_select_proper_newspaper(self):
		response1 = self.client.get('/newspapers/1/')
		response2 = self.client.get('/newspapers/2/')

		self.assertEqual(response1.context['newspaper'], Newspaper.objects.get(pk=1))
		self.assertEqual(response2.context['newspaper'], Newspaper.objects.get(pk=2))