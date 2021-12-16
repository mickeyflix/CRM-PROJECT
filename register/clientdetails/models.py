from django.db import models
from rest_framework import fields


# Create your models here.
class client(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField(max_length=1000)
    courseinterest=models.CharField(max_length=1000)
    isclaimed=models.BooleanField(blank=True,null=True)
    claimedby=models.CharField(max_length=1000,blank=True,null=True)
