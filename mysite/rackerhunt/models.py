# Create your models here.
import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Jobs(models.Model):
    jobTitle = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    segments = models.CharField(max_length=200)
    exp = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)

class github_results(models.Model):
    name = models.CharField(max_length=200)
    pic_url = models.CharField(max_length=1000)
    num_followers = models.IntegerField()
    github_field = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class user_details(models.Model):
    ugithub_name= models.CharField(max_length=200)
    uname= models.CharField(max_length=200)
    upic_url= models.CharField(max_length=1000)
    urepos_url= models.CharField(max_length=500)
    ucompany= models.CharField(max_length=200) 
    ulocation= models.CharField(max_length=200)
    uemail= models.CharField(max_length=200)
    ublog_url= models.CharField(max_length=1000)
    unum_repos= models.IntegerField()
    unum_followers= models.IntegerField()
    unum_following= models.IntegerField()
    ujoined_on= models.CharField(max_length=100)
    ubio= models.CharField(max_length=2000)
