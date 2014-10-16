from django.db import models
from newspapers.models import Newspaper


class Ad(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField()
	newspapers = models.ManyToManyField(Newspaper)
	objects = models.Manager()

	def free(self):
		all_newspapers = Newspaper.objects.all()
		return [item for item in all_newspapers if item not in self.newspapers.all() ]

