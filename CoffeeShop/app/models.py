from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50, blank=True)
    email=models.EmailField(blank=True)
    phone=models.IntegerField(max_length=11,blank=True)
    desc=models.TextField(blank=True)
    

class Review(models.Model):
    name= models.CharField(max_length=50, blank=True)
    desc=models.TextField(blank=True)

class Payment(models.Model):
    name= models.CharField(max_length=50, blank=True)
    cnum=models.IntegerField(blank=True)
    edate=models.DateField(blank=True)
    cvv=models.IntegerField(blank=True)