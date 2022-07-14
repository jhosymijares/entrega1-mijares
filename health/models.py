from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField()

class Booking(models.Model):
    id_client = models.IntegerField()
    id_service = models.IntegerField()
    creation = models.DateTimeField()
    note = models.CharField(max_length=200)
