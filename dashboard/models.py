from django.db import models
from django.contrib.auth.models import User
import django
# Create your models here.

import datetime

class Chore(models.Model):
    """A chore that needs to be done by a single person in a certain interval"""

    name = models.CharField(max_length=50, help_text='Enter the chore name')
    description = models.TextField(help_text='Enter the description for the chore')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Scheduler(models.Model):
    """Schedules the rotation of chores"""

    start = models.DateField(default=django.utils.timezone.now)
