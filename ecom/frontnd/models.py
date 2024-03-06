from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    
class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
    
class cart(models.Model):
    image = models.ImageField(upload_to='media', null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    productname = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)

