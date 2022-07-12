from django.db import models

# Create your models here.

class client(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()

class service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField()

class booking(models.Model):
    idclient = models.IntegerField()
    idservice = models.IntegerField()
    creation = models.DateField()
    note = models.CharField(max_length=200)
