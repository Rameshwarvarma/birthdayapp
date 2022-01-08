from django.db import models
from datetime import date


# Create your models here.
class Birthday(models.Model):
    name = models.CharField(max_length=50)
    Date_of_birth = models.DateField()

    def isBirthdayToday(self):
        # month = Birthday.objects.dates('Date_of_birth', 'month')
        # day = Birthday.objects.dates('Date_of_birth', 'day')
        return date.today().month == self.Date_of_birth.month and date.today().day == self.Date_of_birth.day

    def __str__(self):
        return self.name
