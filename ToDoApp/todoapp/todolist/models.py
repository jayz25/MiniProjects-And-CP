from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    '''ToDoList Name That Inherits models.Model'''
    title = models.CharField(max_length=250) #Varchar
    content = models.TextField(blank=True) #A Text Field
    completed = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    '''A Date Field '''
    def __str__(self):
        return self.title
        #The Name to be shown when called
