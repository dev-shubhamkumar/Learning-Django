from django.db import models

# Create your models here.
# NOTE: Django automatically create database from models.
# NOTE: It creates 1 table in database per model

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

# NOTE: Building a one-to-many relationship b/w location and meetups
# i.e. One location can be used for many meetups
# but not vice versa

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)    # If the location gets deleted then Meetup will also get deleted
    participants = models.ManyToManyField(Participant, blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'