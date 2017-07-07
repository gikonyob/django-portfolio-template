#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from portfolio.models import UserPortfolioModel

class UserPortfolioForm(ModelForm):
	class Meta:
		model = UserPortfolioModel
		exclude = ("middle",)
			