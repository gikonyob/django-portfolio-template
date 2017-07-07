from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from portfolio.forms import UserPortfolioForm
from portfolio.models import UserPortfolioModel
import random
import time
import re

# Create your views here.
def create_portfolio(request):
	title = "Update Your Portfolio"
	disabled = 'disabled'
	user = UserPortfolioModel.objects.all()
	if user.count() < 1:
		disabled = ''
	return render_to_response('port_form.html', {'title': title, 'disabled':disabled})

@csrf_exempt
def insert_to_database(request):
	if request.method == 'POST':
		print request.POST
		print request.FILES
		form = UserPortfolioForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			form = UserPortfolioForm()
	return HttpResponseRedirect('/create_portfolio')

def home(request):
	title = "Home"
	user = UserPortfolioModel.objects.get(first='Brian', last='Wachira')
	first = user.first
	middle = user.middle
	last = user.last
	profile = user.profile
	bio = user.bio
	fun_facts = user.fun_facts.splitlines()
	likes = user.likes.splitlines()
	skills = user.skills.splitlines()
	modified_skills = ["I am skilled in " + skill for skill in skills]
	name = first + " " + last
	return render_to_response('index.html', {'title': title, 'name': name, 'profile': profile, 'description': bio })

def about_me(request):
	user = UserPortfolioModel.objects.get(first='Brian', last='Wachira')
	title = "About " + user.first
	bio = user.bio
	profile = user.profile
	skills = user.skills.splitlines()
	my_projects = user.projects.splitlines()
	pattern = re.compile(r"(https://.*)")
	projects = [pattern.search(re.sub(r'[(|)]',r'', project)).group() for project in my_projects]
	return render_to_response('about.html', {'title': title, 'bio': bio, 'profile': profile, 'skills': skills, 'projects': projects})

def my_profile(request):
	user = UserPortfolioModel.objects.get(first='Brian', last='Wachira')
	first = user.first
	last = user.last
	name = first + " " + last
	title = first + "\'s Profile"
	email = user.email
	secondary_email = user.second_email
	other_email = user.other_email
	profile = user.profile
	tel = user.tel
	fun_facts = user.fun_facts.splitlines()
	fav_quotes = user.fav_quotes.splitlines()
	return render_to_response('profile.html', {'name': name, 'title': title, 'profile': profile, 'email': email, 'secondary_email': secondary_email, 'other_email': other_email,
		'tel': tel, 'fun_facts': fun_facts, 'fav_quotes': fav_quotes})

def my_likes(request):
	user = UserPortfolioModel.objects.get(first='Brian', last='Wachira')
	title = user.first + "\'s Interests"
	likes = user.likes.splitlines()
	profile = user.profile
	return render_to_response('likes.html', {'title': title, 'profile': profile, 'likes': likes})

def my_contacts(request):
	user = UserPortfolioModel.objects.get(first='Brian', last='Wachira')
	title = user.first + "\'s Contacts"
	profile = user.profile
	tel = user.tel
	email = user.email
	secondary_email = user.second_email
	other_email = user.other_email
	facebook = user.facebook
	linkedin = user.linkedin
	github = user.github
	bitbucket = user.bitbucket
	return render_to_response('contacts.html', {'title': title, 'profile': profile, 'tel': tel, 'email': email, 'secondary_email': secondary_email, 'other_email': other_email,
	 'facebook': facebook, 'linkedin': linkedin, 'github': github, 'bitbucket': bitbucket})

