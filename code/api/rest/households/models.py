from django.db import models

# Create your models here.
class EnergyControlling(models.Model):
    name = models.CharField(max_length=50)
    ec_type = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    system_type = models.CharField(max_length=50)
    counter = models.CharField(max_length=50)
    tasks = models.CharField(max_length=50)
