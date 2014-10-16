from django.test import TestCase
from django.http import HttpRequest
from ads.views import create_ad
from ads.models import Ad
from newspapers.models import Newspaper

class HomePageTest(TestCase):

	def test_homepage_uses_proper_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'index.html')


class CreateAdTest(TestCase):

	def test_uses_proper_template(self):
		response = self.client.get('/ads/create/')
		self.assertTemplateUsed(response, 'create_ad.html')

	def test_save_ad_on_post(self):
		response = self.client.post(
			'/ads/create/',
			data={'name': 'Test Ad 1', 'content': 'Buy our stuff now'}
		)
		
		self.assertEqual(Ad.objects.count(), 1)
		new_ad = Ad.objects.first()
		self.assertEqual(new_ad.name, 'Test Ad 1')
		self.assertEqual(new_ad.content, 'Buy our stuff now')

	def test_redirect_after_save(self):
		response = self.client.post(
			'/ads/create/',
			data={'name': 'Test Ad 1', 'content': 'Buy our stuff now'}
		)

		new_ad = Ad.objects.first()
		self.assertRedirects(response, 'ads/%d/' % (new_ad.id))


class AdDetailTest(TestCase):

	def setUp(self):
		ad1 = Ad()
		ad1.name = 'Test Ad 1'
		ad1.content = 'Content 1'
		ad1.save()

		ad2 = Ad()
		ad2.name = 'Test Ad 2'
		ad2.content = 'Content 2'
		ad2.save()

	def test_ad_detail_uses_proper_template(self):
		response = self.client.get('/ads/1/')
		self.assertTemplateUsed(response, 'ad_detail.html')

	def test_select_proper_ad(self):
		response1 = self.client.get('/ads/1/')
		response2 = self.client.get('/ads/2/')

		self.assertEqual(response1.context['ad'], Ad.objects.get(pk=1))
		self.assertEqual(response2.context['ad'], Ad.objects.get(pk=2))


class AdListTest(TestCase):

	def test_ad_list_uses_proper_template(self):
		response = self.client.get('/ads/')
		self.assertTemplateUsed(response, 'ad_list.html')


class ConnectNewspaperTest(TestCase):

	def setUp(self):
		newspaper1 = Newspaper(name='Test Newspaper 1')
		newspaper1.save()

		ad = Ad()
		ad.name = 'Name 1'
		ad.content = 'Content 1'
		ad.save()

	def test_newspaper_gets_connected_to_ad(self):
		response = self.client.post(
			'/ads/1/connect/',
			data={'newspaper_id':1}
		)
		ad = Ad.objects.get(id=1)

		self.assertEqual(ad.newspapers.count(), 1)

class DisonnectNewspaperTest(TestCase):

	def setUp(self):
		newspaper1 = Newspaper(name='Test Newspaper 1')
		newspaper1.save()

		newspaper2 = Newspaper(name='Test Newspaper 2')
		newspaper2.save()

		ad = Ad()
		ad.name = 'Name 1'
		ad.content = 'Content 1'
		ad.save()
		ad.newspapers.add(newspaper1, newspaper2)
		ad.save()

	def test_newspaper_gets_connected_to_ad(self):
		response = self.client.post(
			'/ads/1/disconnect/',
			data={'newspaper_id':1}
		)
		ad = Ad.objects.get(id=1)

		self.assertEqual(ad.newspapers.count(), 1)
