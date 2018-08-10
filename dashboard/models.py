from django.db import models
import datetime

# Create your models here.

class Chore(models.Model):
    """A chore that needs to be done by a single person in a certain interval"""

    name = models.CharField(max_length=50, help_text='Enter the chore name')
    description = models.TextField(help_text='Enter the description for the chore')
    date_start = models.DateField(default=datetime.date.today)

    def week_from_today():
        return datetime.date.today() + datetime.timedelta(days=7)

    date_end = models.DateField(default=week_from_today)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
