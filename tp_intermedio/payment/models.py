from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Payment(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=40)
    days = models.IntegerField()
    
   
    
    def __str__(self):
        return f"{self.code} {self.name} | days: {self.days}"