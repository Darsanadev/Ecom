from django.db import models

# Create your models here.

class Datas(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='media')

class Product(models.Model):
    cname = models.CharField(max_length=100, null=True)
    pname = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    prize = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='media')

class Category(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='media')
