import os
import random
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

def unique_photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(10))
    return 'profile_photos/{id}/{basename}{randomstring}{ext}'.format(id=instance.user.id, basename=basefilename, randomstring=randomstr, ext=file_extension)


class User(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)
    middle_name = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.email

class Skills(models.Model):
    name = models.CharField(max_length=150)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Quotes(models.Model):
    quote = models.TextField(blank=True)
    quoter = models.CharField(max_length=100)

    def __str__(self):
        return self.quote

class Projects(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField(max_length=255)
    site = models.URLField(max_length=255)

    def __str__(self):
        return self.name

class Interests(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class FunFacts(models.Model):
    fact = models.TextField(blank=True)
    who_by = models.CharField(max_length=150)

    def __str__(self):
        return self.fact

class Repositories(models.Model):
    repository_name = models.CharField(max_length=150)
    url = models.URLField(max_length=255)
    site = models.URLField(max_length=255)

    def __str__(self):
        return self.repository_name

class Social(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField(max_length=255)
    site = models.URLField(max_length=255)

    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secondary_email = models.EmailField(max_length=60, unique=True)
    telephone_no = models.CharField(max_length=13, blank=True)
    secondary_telephone_no = models.CharField(max_length=13, blank=True)
    date_of_birth = models.DateField(default=datetime.datetime(1900, 1, 1))
    profile_picture = models.ImageField(upload_to=unique_photo_path, default='profile_photos/user.png')
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField(Skills, related_name="user_skills")
    quotes = models.ManyToManyField(Quotes, related_name="user_quotes")
    projects = models.ManyToManyField(Projects, related_name="user_projects")
    fun_facts = models.ManyToManyField(FunFacts, related_name="user_facts")
    interests = models.ManyToManyField(Interests, related_name="user_interests")
    repositories = models.ManyToManyField(Repositories, related_name="user_repos")
    socials = models.ManyToManyField(Social, related_name="user_socials")
    articles = models.ManyToManyField(Articles, related_name="user_articles")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()