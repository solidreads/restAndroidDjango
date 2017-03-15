from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
	cedulaPer = models.SmallIntegerField()
	apellidoPer = models.CharField(max_length=50)
	nombrePer = models.CharField(max_length=50)

	def __str__(self):
		return self.apellidoPer