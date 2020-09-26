from django.db import models
from django.forms import fields
import uuid
from macaddress import default_dialect
from netaddr import EUI, mac_bare
from macaddress import format_mac
from macaddress.fields import MACAddressField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Session(models.Model):
    Mac = models.CharField(max_length=100)
    Auth0_Token = models.CharField(max_length=100)


class Search(models.Model):
    Session = models.ForeignKey(Session, related_name='Session+', on_delete=models.CASCADE)
    keywords = models.CharField(max_length=100)
    
    
class Product(models.Model): 
    Session = models.ForeignKey(Session, related_name='Session+', on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Price=models.CharField(max_length=500)
    Description=models.CharField(max_length=10000)
    Url=models.CharField(max_length=500)

class Mouse_Click(models.Model):   
    Session = models.ForeignKey(Session, related_name='Session+', on_delete=models.CASCADE)
    Element=models.CharField(max_length=100)

class Cart(models.Model):    
    Session = models.ForeignKey(Session, related_name='Session+', on_delete=models.CASCADE)
    Request = models.CharField(max_length=1000000) 

class Add_To_Cart(models.Model):   
    Session = models.ForeignKey(Session, related_name='Session+', on_delete=models.CASCADE)
    Product_name=models.CharField(max_length=100)
    Url=models.CharField(max_length=500)

class Delete_From_The_Cart(models.Model):    
    Session = models.ForeignKey(Session, related_name='Session+', on_delete=models.CASCADE)
    Product_name=models.CharField(max_length=100)
    Url=models.CharField(max_length=500)

class Checkout(models.Model):    
    Session = models.ForeignKey(Session, related_name='Session+', on_delete=models.CASCADE)
    Request = models.CharField(max_length=1000000) 