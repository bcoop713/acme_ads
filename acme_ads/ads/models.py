from django.db import models


class Ad(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField()
