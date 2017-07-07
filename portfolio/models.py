from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserPortfolioModel(models.Model):
	first = models.CharField(max_length=15)
	middle = models.CharField(max_length=15, null=True, default='')
	last = models.CharField(max_length=15)
	email = models.EmailField(max_length=50)
	second_email = models.EmailField(null=True)
	other_email = models.EmailField(null=True)
	profile = models.ImageField(upload_to='images', null=True)
	tel = models.CharField(max_length=13)
	facebook = models.URLField(null=True)
	linkedin = models.URLField(null=True)
	github = models.URLField(null=True)
	bitbucket = models.URLField(null=True)
	bio = models.TextField(null=True)
	skills =models.TextField(null=True)
	fav_quotes = models.TextField(null=True)
	fun_facts = models.TextField(null=True)
	projects = models.TextField(null=True)
	likes = models.TextField(null=True)

	def __unicode__(self):
		return first

