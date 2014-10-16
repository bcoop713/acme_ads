from django.test import TestCase
from ads.models import Ad
from newspapers.models import Newspaper


class AdModelTest(TestCase):

	def setUp(self):
		newspaper1 = Newspaper(name='Test Newspaper 1')
		newspaper1.save()

		newspaper2 = Newspaper(name='Test Newspaper 2')
		newspaper2.save()

		newspaper3 = Newspaper(name='Test Newspaper 3')
		newspaper3.save()

		first_ad = Ad()
		first_ad.name = 'Name 1'
		first_ad.content = 'Content 1'
		first_ad.save()
		first_ad.newspapers.add(newspaper1, newspaper2)
		first_ad.save()

		second_ad = Ad()
		second_ad.name = 'Name 2'
		second_ad.content = 'Content 2'
		second_ad.save()
		second_ad.newspapers.add(newspaper2, newspaper3)
		first_ad.save()

	def test_saving_and_retrieving_ads(self):
		newspapers = Newspaper.objects.all()

		saved_ads = Ad.objects.all()
		self.assertEqual(saved_ads.count(), 2)

		first_saved_ad = saved_ads[0]
		second_saved_ad = saved_ads[1]
		self.assertEqual(first_saved_ad.name, 'Name 1')
		self.assertEqual(first_saved_ad.content, 'Content 1')
		self.assertSequenceEqual(first_saved_ad.newspapers.all(), [newspapers[0], newspapers[1]])

		self.assertEqual(second_saved_ad.name, 'Name 2')
		self.assertEqual(second_saved_ad.content, 'Content 2')
		self.assertSequenceEqual(second_saved_ad.newspapers.all(), [newspapers[1], newspapers[2]])

	def test_free_newspaper_list(self):
		newspapers = Newspaper.objects.all()
		saved_ads = Ad.objects.all()
		
		self.assertSequenceEqual(saved_ads[0].free(), [newspapers[2]])
		self.assertSequenceEqual(saved_ads[1].free(), [newspapers[0]])

