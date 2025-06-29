from django.db import models
from datetime import datetime
# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=1000,blank=True)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now,blank=True)
    finished_date = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True) 
   
    def __str__(self):
        return self.title