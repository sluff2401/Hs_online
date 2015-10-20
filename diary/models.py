import datetime
from django.db import models
from django.utils import timezone

class Event(models.Model):
    event_date       = models.DateField('Event date in the format yyyy-mm-dd, e.g for the 24th of August 2015, enter 2015-08-24',max_length=10)
    reference        = models.CharField(max_length=100)
    text             = models.TextField('Event details')
    status           = models.BooleanField(default=True)
    def __str__(self):               
        return self.reference
    def publish(self):
        self.save()

  
