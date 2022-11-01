import email
from pyexpat import model
from sqlite3 import Date
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
         
class Manager(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    place = models.CharField(max_length=100)
    local = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.place + " " + self.local + " " + self.district + " " + self.state

class Scheduler(models.Model):
    Date = models.DateField()
    AM5 = models.BooleanField(default=False)
    AM6 = models.BooleanField(default=False)
    AM7 = models.BooleanField(default=False)
    AM8 = models.BooleanField(default=False)
    AM9 = models.BooleanField(default=False)
    AM10 = models.BooleanField(default=False)
    AM11 = models.BooleanField(default=False)
    AM12 = models.BooleanField(default=False)
    PM1 = models.BooleanField(default=False)
    PM2 = models.BooleanField(default=False)
    PM3 = models.BooleanField(default=False)
    PM4 = models.BooleanField(default=False)
    PM5 = models.BooleanField(default=False)
    PM6 = models.BooleanField(default=False)
    PM7 = models.BooleanField(default=False)
    PM8 = models.BooleanField(default=False)
    PM9 = models.BooleanField(default=False)
    PM10 = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Date)

class Booked(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=50)
    slot_date = models.CharField(max_length=100)
    slot_time = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.slot_date


    