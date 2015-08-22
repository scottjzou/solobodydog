from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField(default=-1)
    register_date = models.DateTimeField(auto_now_add=True)


class LoginHistory(models.Model):
    user = models.ForeignKey(AuthUser)
    login_date = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.ForeignKey(AuthUser)
    birthday = models.DateTimeField(blank=True, null=True)
    job = models.CharField(max_length=60)
    hobbies = models.CharField(max_length=400)
    about = models.CharField(max_length=400, null=True, blank=True)
    skills = ArrayField(models.CharField(max_length=30), null=True, blank=True)


class Event(models.Model):
    user = models.ForeignKey(AuthUser)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=2000, null=True, blank=True)
    # invitee = ArrayField(AuthUser(), default=[], null=True, blank=True)