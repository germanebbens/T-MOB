from django.db import models
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Redirect(models.Model):
    id = models.BigAutoField(primary_key=True) 
    key= models.SlugField(max_length=200, unique=True)
    url= models.URLField(max_length = 200)
    active= models.BooleanField()
    upddate_at= models.DateTimeField(auto_now=True) #https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.DateField.auto_now
    created_at= models.DateTimeField(auto_now_add=True) #https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.DateField.auto_now_add

