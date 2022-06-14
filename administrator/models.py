from django.db import models
from django.urls import reverse



class school(models.Model):

	stname = models.CharField(max_length=15)

	stcls = models.IntegerField()

	stroll = models.IntegerField()

	staddr = models.CharField(max_length=150)

	def __str__(self):

		return self.stname +'|' + str(self.stcls)

	def get_absolute_url(self):

		return reverse('home')