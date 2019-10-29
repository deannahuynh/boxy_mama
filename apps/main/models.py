from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email


class AddressManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['street_address']) < 5:
            errors["street_address"] = "Street address must be at least 5 characters"
        if len(postData['city']) < 1:
            errors["city"] = "City is required"
        if len(postData['country']) < 1:
            errors["password"] = "Country is required"
        if len(postData['zip']) < 5:
            errors["zip"] = "Zipcode is required"
        return errors

class OrderManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['box_theme']) < 1:
            errors["theme"] = "Please select a theme"
        if len(postData['first_name']) < 1:
            errors["title"] = "First Name must be at least 1 Character"
        if len(postData['last_name']) < 1:
            errors["desc"] = "Last Name must be at least 1 Character"
        if len(postData['email']) < 2:
            errors["email"] = "Email Address must be valid"
        if len(postData['note']) < 1:
            errors["note"] = "Please Leave a note for your loved one :) - XOXO Boxy Mama"
        return errors

class Address(models.Model):
    street_address= models.CharField(max_length=200)
    address_2= models.CharField(max_length=200, null=True, blank=True)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=50)
    zip_code= models.IntegerField()
    country= models.CharField(max_length=200)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    objects = AddressManager()
    
class Order(models.Model):
    box_theme= models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    note = models.TextField()
    address = models.ForeignKey(Address, related_name= "orders")
    objects = OrderManager()
