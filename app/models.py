from django.db import models

# Create your models here.
class Webpage(models.Model):
    Topic_name=models.CharField(max_length=100)
    Name=models.CharField(max_length=200)
    Date=models.DateField()