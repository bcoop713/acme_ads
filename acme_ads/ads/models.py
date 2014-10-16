from django.db import models
from newspapers.models import Newspaper


class Ad(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField()
	newspapers = models.ManyToManyField(Newspaper)
