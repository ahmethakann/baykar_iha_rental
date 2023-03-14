from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

class Location(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
class IhaDealer(models.Model):
    iha_dealer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone =  models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(50)], max_length = 50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    earnings = models.IntegerField(default=0)
    type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.iha_dealer)
    
class Iha(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to="media")
    iha_dealer = models.ForeignKey(IhaDealer, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    rent = models.CharField(max_length=50, blank=True)
    operational_altitude = models.CharField(max_length=50, blank=True, null=True)
    max_altitude = models.CharField(max_length=50, blank=True, null=True)
    max_flight_time = models.CharField(max_length=50, blank=True, null=True)
    payload_capacity = models.CharField(max_length=50, blank=True, null=True)
    communication_range = models.CharField(max_length=50, blank=True, null=True)
    fuel_capacity = models.CharField(max_length=50, blank=True, null=True)
    cruise_speed = models.CharField(max_length=50, blank=True, null=True)
    max_speed = models.CharField(max_length=50, blank=True, null=True)
    max_takeoff_weight = models.CharField(max_length=50, blank=True, null=True)
    height = models.CharField(max_length=50, blank=True, null=True)
    wingspan = models.CharField(max_length=50, blank=True, null=True)
    lenght = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    type  = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.user)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    iha_dealer = models.ForeignKey(IhaDealer, on_delete=models.CASCADE)
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    rent = models.CharField(max_length=50)
    days = models.IntegerField(default=1, blank=False)
    is_complete = models.BooleanField(default=False)