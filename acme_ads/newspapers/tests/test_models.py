from django.test import TestCase
from newspapers.models import Newspaper


class NewspaperModelTest(TestCase):

	def test_saving_and_retrieving_newspapers(self):
		first_newspaper = Newspaper()
		first_newspaper.name = 'Name 1'
		first_newspaper.save()

		second_newspaper = Newspaper()
		second_newspaper.name = 'Name 2'
		second_newspaper.save()

		saved_newspapers = Newspaper.objects.all()
		self.assertEqual(saved_newspapers.count(), 2)

		first_saved_newspaper = saved_newspapers[0]
		second_saved_newspaper = saved_newspapers[1]
		self.assertEqual(first_saved_newspaper.name, 'Name 1')
		self.assertEqual(second_saved_newspaper.name, 'Name 2')
