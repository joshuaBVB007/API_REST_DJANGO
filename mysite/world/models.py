from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=80)
    capital=models.CharField(max_length=80)

class City(models.Model):
    code_country=models.ForeignKey(Country,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=80)
    major=models.CharField(max_length=80)
    population=models.FloatField(default="no data")

