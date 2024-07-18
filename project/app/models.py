
# Create your models here.
from django.db import models

class car_model(models.Model):
    car_name=models.CharField(max_length=50)
    variety_fuel=models.CharField(max_length=50)
    car_color=models.CharField(max_length=50)

    def __str__(self):
        return self.car_name
class customer(models.Model):
    car_name=models.CharField(max_length=50)
    cus_email=models.EmailField(max_length=50)
    cus_contact=models.IntegerField(null=True)
    car_name=models.ManyToManyField(car_model)