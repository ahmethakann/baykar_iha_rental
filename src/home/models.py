from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

class Location(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
class IhaDealer(models.Model):
    iha_dealer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone =  models.CharField(validators = [MinLengthValidator(50), MaxLengthValidator(50)], max_length = 50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    earnings = models.IntegerField(default=0)
    type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.car_dealer)
    
class Iha(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="")
    iha_dealer = models.ForeignKey(IhaDealer, on_delete=models.PROTECT)
    capacity = models.CharField(max_length=2)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    rent = models.CharField(max_length=50, blank=True)

    operational_altitude = models.CharField(max_length=50)
    max_altitude = models.CharField(max_length=50)
    max_flight_time = models.CharField(max_length=50)
    payload_capacity = models.CharField(max_length=50)
    communication_range = models.CharField(max_length=50)
    fuel_capacity = models.CharField(max_length=50)
    cruise_speed = models.CharField(max_length=50)
    max_speed = models.CharField(max_length=50)
    max_takeoff_weight = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    wingspan = models.CharField(max_length=50)
    lenght = models.CharField(max_length=50)


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
    Iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    rent = models.CharField(max_length=50)
    days = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)