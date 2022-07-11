from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()

class service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField()

class booking(models.Model):
    id_service = models.IntegerField()
    creation = models.DateField()
    note = models.CharField(max_length=200)
