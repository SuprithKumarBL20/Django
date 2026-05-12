from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    job=models.CharField(max_length=50)
    sal=models.FloatField()