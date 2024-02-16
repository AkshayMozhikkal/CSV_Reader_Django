from django.db import models

# Create your models here.

class Bitcoin(models.Model):
    date = models.CharField(max_length = 50 , blank =True, null = True)
    price = models.CharField(max_length = 50 , blank =True, null = True)
    open = models.CharField(max_length = 50 , blank =True, null = True)
    high = models.CharField(max_length = 50 , blank =True, null = True)
    low = models.CharField(max_length = 50 , blank =True, null = True)
    vol = models.CharField(max_length = 50 , blank =True, null = True)
    change = models.CharField(max_length = 50 , blank =True, null = True)
   
