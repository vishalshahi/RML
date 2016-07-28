from __future__ import unicode_literals

from django.db import models

# Create your models here.
class InputDetails(models.Model):
	email = models.CharField(max_length=100)
	phone = models.IntegerField()
	preferred = models.CharField(max_length=100)
	reminder = models.DateTimeField()
