from django.test import TestCase
from ads.models import Ad


class AdModelTest(TestCase):

	def test_saving_and_retrieving_ads(self):
		first_ad = Ad()
		first_ad.name = 'Name 1'
		first_ad.content = 'Content 1'
		first_ad.save()

		second_ad = Ad()
		second_ad.name = 'Name 2'
		second_ad.content = 'Content 2'
		second_ad.save()

		saved_ads = Ad.objects.all()
		self.assertEqual(saved_ads.count(), 2)

		first_saved_ad = saved_ads[0]
		second_saved_ad = saved_ads[1]
		self.assertEqual(first_saved_ad.name, 'Name 1')
		self.assertEqual(first_saved_ad.content, 'Content 1')
		self.assertEqual(second_saved_ad.name, 'Name 2')
		self.assertEqual(second_saved_ad.content, 'Content 2')
