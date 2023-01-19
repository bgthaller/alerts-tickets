
from django.db import models
from simple_history.models import HistoricalRecords
from django.core.validators import MinLengthValidator

# Create your models here.

class ticket(models.Model):
    location= models.CharField(max_length=20, null=True, blank=True)
    date_created= models.DateField(null=True,blank=True)
    date_completed= models.DateField(null=True,blank=True)
    complete=models.BooleanField(default=False)     
    created_by= models.CharField( max_length=30,null=True,blank=True)
    closed_by= models.CharField( max_length=30,null=True,blank=True)
    description= models.CharField(max_length=2000, null=True, blank=True)
    
    def __str__(self):
        return str(self.location)


class abnormal_condition(models.Model):

    LOC_CHOICES = [
        ('Sub 1','Sub 1'),
        ('Sub 2','Sub 2'),
        ('Sub 3','Sub 3'),
       
        ]    

    FEEDER_CHOICES = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
        ]    
   
    Sub=models.CharField(
        max_length=12,
        choices=LOC_CHOICES)
    feeder= models.IntegerField(       
        choices=FEEDER_CHOICES)
    location=models.CharField(max_length=20,null=True,blank=True)
    date_created= models.DateTimeField(null=True,blank=True)
    date_edited=models.DateTimeField(null=True,blank=True)
    date_completed= models.DateTimeField(null=True,blank=True)
    complete=models.BooleanField(default=False)     
   # user_name= models.CharField( max_length=30,null=True,blank=True)
    description= models.CharField(max_length=2000, null=True, blank=True)
    history = HistoricalRecords()
    def __str__(self):
        return str(self.id)