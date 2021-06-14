from django.db import models

# Create your models here.
# NOTE: Django automatically create database from models.
# NOTE: It creates 1 table in database per model

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()