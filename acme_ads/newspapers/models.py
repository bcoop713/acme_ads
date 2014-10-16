from django.db import models


class Newspaper(models.Model):
	name = models.CharField(max_length=30)